from datetime import timezone, timedelta
from zoneinfo import available_timezones
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import request
from .models import *
from django.views.decorators.csrf import csrf_exempt
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from django.http import JsonResponse
import json
from .forms import *
from .utils import *
from django.utils import timezone

template = """
You are a mental health support chatbot designed to engage in open-ended, empathetic conversations. Your role is to be a supportive friend, offering advice and encouragement while respecting boundaries and avoiding any clinical or diagnostic language.

Here is the conversation history: {context}

User Input: {user_input}

When responding, acknowledge the user's emotions and experiences. Offer gentle advice on topics like self-care, stress relief, and resilience, and use a warm and friendly tone to convey understanding and support.

Response:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Store conversation context globally (consider database or session storage in production)


@csrf_exempt
def chatbot_response(request):

    # Ensure conversation history is in the session
    if "conversation_history" not in request.session:
        request.session["conversation_history"] = []

    if request.method == 'POST':
        # Parse the JSON body
        data = json.loads(request.body)
        user_input = data.get('message')

        # Retrieve session-specific context (last messages in history)
        context = "\n".join(
            [f"User: {msg['user']}\nAI: {msg['bot']}" for msg in request.session["conversation_history"]])

        # Generate a response from the model
        result = chain.invoke({"context": context, "user_input": user_input})

        # Append the user and bot messages to the conversation history
        request.session["conversation_history"].append({"user": user_input, "bot": result})

        # Save the updated conversation history in the session
        request.session.modified = True

        # Return the response as JSON to the frontend
        return JsonResponse({'response': result})


def chatbot_page(request):
    # Pass conversation history to the template
    conversation_history = request.session.get("conversation_history", [])
    return render(request, 'chatbot.html', {"conversation_history": conversation_history})





User = get_user_model()

@login_required(login_url='login')
def home(request):
    if request.user.role.role_name == 'counsellor':
        return redirect('counsellor_home')
    else:

        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        if request.method == 'POST':
            mood_value = request.POST.get('mood_value')
            if mood_value:
                current_hour = timezone.now().hour
                time_period = None
                if 0 <= current_hour < 12:
                    time_period = 'morning'
                elif 12 <= current_hour < 17:
                    time_period = 'afternoon'
                elif 17 <= current_hour < 24:
                    time_period = 'evening'

                if time_period:
                    if not MoodTracking.objects.filter(
                        user=request.user,
                        timestamp__date=today,
                        timestamp__hour__gte=current_hour - 3
                    ).exists():
                        MoodTracking.objects.create(user=request.user, mood=int(mood_value), timestamp=timezone.now())
                        messages.success(request, 'Mood tracked successfully.')
                    else:
                        messages.warning(request, 'You have already tracked your mood for this time period.')
                else:
                    messages.error(request, 'Invalid time period.')
            return redirect('home')

        mood_entries = MoodTracking.objects.filter(
            user=request.user,
            timestamp__date__gte=start_of_week,
            timestamp__date__lte=today
        ).order_by('timestamp')

        mood_data = {day: {'morning': None, 'afternoon': None, 'evening': None} for day in days_of_week}

        mood_colors = {
            1: "#FF4D4D",  # Very sad - Red
            2: "#FFA500",  # Sad - Orange
            3: "#FFFF00",  # Neutral - Yellow
            4: "#9ACD32",  # Happy - Light green
            5: "#32CD32",  # Very happy - Green
        }

        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for entry in mood_entries:
            day = entry.timestamp.date()
            day_name = day_names[day.weekday()]
            hour = entry.timestamp.hour

            if 0 <= hour < 12:
                period = 'morning'
            elif 12 <= hour < 17:
                period = 'afternoon'
            elif 17 <= hour < 24:
                period = 'evening'
            else:
                continue

            if day_name in mood_data:
                if mood_data[day_name][period] is None:
                    mood_data[day_name][period] = {
                        'mood': entry.mood,
                        'color': mood_colors[entry.mood]
                    }

        return render(request, 'home.html', {'mood_data': mood_data, 'days_of_week': days_of_week})

@login_required()
def counsellor_home(request):
    if request.user.role.role_name != 'counsellor':
        return redirect('home')
    else:
        return render(request, 'counsellor_home.html')

def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)  # Log the user in
                streak_counter(user)
                messages.success(request, 'log in successful.')
                return redirect('home')  # Redirect to home after successful login
            else:
                # error message
                form.add_error(None, 'Invalid username or password')
    else:
        form = login_form()
    return render(request, 'login.html', {'form': form})

def register(request):
    step = request.GET.get('step') or '1' # Default to step 1

    # Step 1: Initial Register Form
    if step == '1':
        form = register_form(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            if User.objects.filter(email=email).exists():
                messages.error(request, "An account with this email already exists.")
                return redirect('/register?step=1')

            request.session['email'] = email
            request.session['password'] = password
            request.session['role'] = 2 if role else 1
            return redirect('/register?step=2')

    elif step == '2':
        form = user_details_form(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            return redirect('/register?step=3')

    elif step == '3':
        form = extra_details_form(request.POST or None, request.FILES or None)
        if request.method == 'POST' and form.is_valid():
            request.session['bio'] = form.cleaned_data['bio']
            request.session['profile_picture'] = request.FILES.get('profile_picture')
            return redirect('/register?step=4' if request.session.get('role') == 2 else '/register?step=complete')

    elif step == '4':
        form = register_counsellor_form(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            request.session['specialization'] = form.cleaned_data['specialization']
            request.session['qualification'] = form.cleaned_data['qualification']
            request.session['experience_years'] = form.cleaned_data['experience_years']
            request.session['counsellor_bio'] = form.cleaned_data['bio']
            return redirect('/register?step=5')

    elif step == '5':
        form = counsellor_availability_form(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            request.session['availability'] = {
                'date': form.cleaned_data['date'].isoformat(),
                'start_time': form.cleaned_data['start_time'],
                'duration': str(form.cleaned_data['duration'])
            }
            return redirect('/register?step=complete')

    elif step == "complete":
        try:
            user = User.objects.create_user(
                email=request.session['email'],
                password=request.session['password'],
                first_name=request.session.get('first_name'),
                last_name=request.session.get('last_name'),
                bio=request.session.get('bio'),
                location=request.session.get('location'),
                profile_picture=request.session.get('profile_picture'),
            )
            user.role = Role.objects.get(role_id=request.session.get('role'))
            user.save()

            if request.session.get('role') == 2:
                counsellor_profile = CounsellorProfile.objects.create(
                    user=user,
                    specialization=request.session.get('specialization'),
                    qualification=request.session.get('qualification'),
                    experience_years=request.session.get('experience_years'),
                    bio=request.session.get('counsellor_bio')
                )
                availability_data = request.session.get('availability')
                availability_date = datetime.fromisoformat(availability_data['date']).date()
                start_time = datetime.strptime(availability_data['start_time'], '%H:%M').time()
                duration_parts = list(map(int, availability_data['duration'].split(':')))
                duration = timedelta(hours=duration_parts[0], minutes=duration_parts[1], seconds=duration_parts[2])
                CounsellorAvailability.objects.create(
                    counsellor=counsellor_profile,
                    date=availability_date,
                    start_time=start_time,
                    duration=duration
                )
            auth_login(request, user)
            streak_counter(user)
            messages.success(request, "Registration successful!")
            # Clear session data
            for key in [
                'email', 'password', 'first_name', 'last_name', 'bio',
                'profile_picture', 'specialization', 'qualification',
                'experience_years', 'counsellor_bio', 'availability', 'role'
            ]:
                request.session.pop(key, None)
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('/register?step=1')

    return render(request, 'register.html', {'form': form, 'step': step})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def user_details(request):
    form = SaveUserDetails(instance=request.user)  # Pass the logged-in user's instance

    if request.method == 'POST':
        form = SaveUserDetails(request.POST, request.FILES, instance=request.user)  # Update the instance
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'user_details.html', context)

@login_required
def video_call(request):
    return render(request, 'video_call.html')

@login_required
def professionals(request):
    return render(request, 'professionals.html')

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user, status='pending').order_by('date')
    counsellors = CounsellorProfile.objects.all()

    counsellor_id = request.GET.get('counsellor_id')
    if counsellor_id:
        bookings = bookings.filter(availability__counsellor_id=counsellor_id)

    # Handle sorting by date
    sort_by = request.GET.get('sort_by', 'asc')
    if sort_by == 'desc':
        bookings = bookings.order_by('-date')
    else:
        bookings = bookings.order_by('date')

    if request.method == 'POST':
        # Handle cancellation if a cancel button is pressed
        booking_id = request.POST.get('booking_id')
        if booking_id:
            booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
            booking.status = 'canceled'
            if booking.availability:
                booking.availability.is_available = True
                booking.availability.save()
            booking.save()
            messages.success(request, 'Booking canceled successfully.')
            return redirect('view_bookings')

    return render(request, 'view_bookings.html', {'bookings': bookings, 'counsellors':counsellors})

@login_required()
def rebook(request, counsellor_id):
    counsellor = get_object_or_404(CounsellorProfile, counsellor_id=counsellor_id)
    availability = counsellor.availability.filter(is_available=True)  # Get available slots

    if request.method == 'POST':
        user = request.user
        session_id = request.POST.get('session_id')
        try:
            selected_availability = CounsellorAvailability.objects.get(availability=session_id)
            # Create a new booking and set status
            booking = Booking.objects.create(
                user=user,
                availability=selected_availability,
                booking_date=datetime.today().date(),
                status="pending"  # Set the status to pending
            )
            selected_availability.is_available = False
            selected_availability.save()

            messages.success(request, "Booking successful!")
            return redirect('view_bookings')  # Redirect to view bookings

        except CounsellorAvailability.DoesNotExist:
            messages.error(request, "No available session for this counsellor.")
            return redirect('professionals')

    return render(request, 'book_session.html', {
        'counsellor': counsellor,
        'availability': availability
    })

@login_required
def book_session(request, counsellor_id):
    counsellor = get_object_or_404(CounsellorProfile, counsellor_id=counsellor_id)
    availability = counsellor.availability.filter(is_available=True)
    if request.method == 'POST':
        user = request.user
        session_id = request.POST.get('session_id')
        try:
            selected_availability = CounsellorAvailability.objects.get(availability=session_id)

            # Create booking and mark availability as booked
            booking = Booking.objects.create(
                user=user,
                availability=selected_availability,
                date=datetime.today().date(),
                status="pending"
            )
            selected_availability.is_available = False
            selected_availability.save()

            messages.success(request, "Booking successful!")
        except CounsellorAvailability.DoesNotExist:
            messages.error(request, "No available session for this counsellor.")
            return redirect('professionals')

        return render(request, 'book_session.html', {
            'counsellor': counsellor,
            'availability': availability
        })

    return render(request, 'book_session.html', {
        'counsellor': counsellor,
        'availability': availability
    })

@login_required()
def set_availability(request):
    if request.user.role.role_name != 'counsellor':
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    if request.method == 'POST':
        form = counsellor_availability_form(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.counsellor = request.user.counsellorprofile

            if CounsellorAvailability.objects.filter(
                counsellor=availability.counsellor,
                date=availability.date,
                start_time=availability.start_time,
            ).exists():
                messages.error(request, "Availability for this time already exists.")
            else:
                availability.save()
                messages.success(request, "Availability successfully set!")
            return redirect('set_availability')
    else:
        form = counsellor_availability_form()

    return render(request, 'set_availability.html', {'form': form})
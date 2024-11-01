from .models import *

def user_context(request):

    user = request.user
    counsellors = User.objects.filter(role_id=2)
    counsellor_details = CounsellorProfile.objects

    return {
        'user': user,
        'counsellors': counsellors,
        'counsellor_details': counsellor_details
    }
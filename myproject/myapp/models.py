from django.db import models

# 1. Roles Table
class Role(models.Model):
    class Meta:
        db_table = 'roles'
    role_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    role_name = models.CharField(max_length=255)
    permissions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role_name

# 2. Users Table
class User(models.Model):
    class Meta:
        db_table = 'users'

    user_id = models.CharField(max_length=10, primary_key=True, serialize=False)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# 3. Sessions Table
class Session(models.Model):
    class Meta:
        db_table = 'sessions'
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Session {self.session_id} - {self.status}"

# 4. Counsellor Profiles Table
class CounsellorProfile(models.Model):
    class Meta:
        db_table = 'counsellor_profiles'
    counsellor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.specialization}"

# 5. Bookings Table
class Booking(models.Model):
    class Meta:
        db_table = 'bookings'
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    counsellor = models.ForeignKey('CounsellorProfile', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Booking {self.booking_id} - {self.status}"

# 6. Chat Logs Table
class ChatLog(models.Model):

    class Meta:
        db_table = 'chat_logs'
    chat_id = models.AutoField(primary_key=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    sender = models.ForeignKey('User', related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey('User', related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.chat_id} - {self.message[:30]}..."

# 7. Call Logs Table
class CallLog(models.Model):

    class Meta:
        db_table = 'call_logs'
    call_id = models.AutoField(primary_key=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    caller = models.ForeignKey('User', related_name='caller', on_delete=models.CASCADE)
    callee = models.ForeignKey('User', related_name='callee', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Call {self.call_id} - {self.status}"

# 8. Mood Tracking Table
class MoodTracking(models.Model):
    class Meta:
        db_table = 'mood_tracking'
    mood_entry_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    mood = models.IntegerField()
    entry_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Mood {self.mood_entry_id} - Mood: {self.mood}"

# 9. Counsellor Availability Table
class CounsellorAvailability(models.Model):
    class Meta:
        db_table = 'counsellor_availabilities'
    availability_id = models.AutoField(primary_key=True)
    counsellor = models.ForeignKey('CounsellorProfile', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.counsellor.user.full_name} - {self.day_of_week}"

# 10. Notifications Table
class Notification(models.Model):
    class Meta:
        db_table = 'notifications'
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Notification {self.notification_id} for {self.user}"

# 11. Chatbot Logs Table
class ChatbotLog(models.Model):
    class Meta:
        db_table = 'chatbot_logs'
    chatbot_log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    input_message = models.TextField()
    response_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chatbot Log {self.chatbot_log_id} for {self.user.username}"

# 12. Payment History Table
class PaymentHistory(models.Model):
    class Meta:
        db_table = 'payment_history'
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount}"

# 13. Subscription Plans Table
class SubscriptionPlan(models.Model):
    class Meta:
        db_table = 'subscription_plans'
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=255)
    plan_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.plan_name

# 14. User Subscriptions Table
class UserSubscription(models.Model):
    class Meta:
        db_table = 'user_subscriptions'
    subscription_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    plan = models.ForeignKey('SubscriptionPlan', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"Subscription {self.subscription_id} for {self.user.username}"

from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Booking)
admin.site.register(CallLog)
admin.site.register(ChatbotLog)
admin.site.register(ChatLog)
admin.site.register(CounsellorAvailability)
admin.site.register(CounsellorProfile)
admin.site.register(MoodTracking)
admin.site.register(Notification)
admin.site.register(Role)
admin.site.register(PaymentHistory)
admin.site.register(Session)
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)

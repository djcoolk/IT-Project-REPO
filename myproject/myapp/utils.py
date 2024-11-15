import hashlib
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import connection
from .models import *


def streak_counter(user):
    current_date = datetime.today().date()
    if user.last_login:
        last_login_date = user.last_login.date()

        if current_date == last_login_date + timedelta(days=1):
            user.login_streak += 1
        elif current_date != last_login_date:
            user.login_streak = 1
    else:
        user.login_streak = 1

    user.save()

#     def book():
#
#     def chat():
#
#     def call():
#
#     def track_mood():
#
#     def notifiy():
#
#     def subscribe():

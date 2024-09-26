from django.db import models

# Create your models here.

class UserDetails(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    role_id = models.CharField(max_length=3)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_verified = models.CharField(max_length=1)

    def __str__(self):
        return self.full_name
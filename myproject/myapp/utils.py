import hashlib
from django.db import connection

class User:
    # Order of attributes has to match order of fields in DB in order for unpack operator to work properly
    def __init__(self,id, role, username, email, password_hash, full_name,profile_picture, bio,  location, last_login, isVerified):
        self.id = id
        self.role = role
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.full_name = full_name
        self.bio = bio
        self.profile_picture = profile_picture
        self.location = location
        self.last_login = last_login
        self.isVerified = isVerified

    def login(username, password):
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest() ## hash password using sha256 for security
        #password_hash = password # for testing only

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username=%s AND password_hash=%s", [username, password_hash])
            user_details = cursor.fetchone()
        if user_details is None:
            return None
        else:
            return User(*user_details)  # unpack operator "*" will populate attributes for user object.

    def register(email, username, password):
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest() ## hash password using sha256 for security
        #password_hash = password  ## for testing

        with connection.cursor() as cursor: #check if user exists if user doesnt exist create new record
            cursor.execute("SELECT user_id FROM users WHERE username=%s OR email=%s", [username, email])
            existing_user = cursor.fetchone()
            if existing_user is None:
                cursor.execute("INSERT INTO users (email, username, password_hash) values (%s,%s,%s)" ,[email, username, password_hash])
                cursor.execute("SELECT user_id FROM users WHERE username=%s", [username])
                user_id = cursor.fetchone()
                return user_id[0]
            else:
                return None

    def saveDetails(self):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE users SET users WHERE user_id=%s", [self.id])

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
#
# class therapist:
#     def login(username, password):
#     def register(email, username, password):
#     def book():
#     def chat():
#     def call():
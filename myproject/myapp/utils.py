import hashlib
from django.db import connection

class user:
    def login(username, password):
        # password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest() ## hash password using sha256 for security
        password_hash = password ## for testing

        with connection.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users WHERE username=? AND password_hash=?", [username, password_hash])
            user_id = cursor.fetchone()[0]

        if user_id is None:
            return None
        else:
            return user_id
from .models import *

def user_context(request):

    user = request.user if request.user.is_authenticated else None
    counsellors = User.objects.filter(role_id=2)

    return {
        'user': user,
        'counsellors': counsellors
    }
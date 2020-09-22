# THIS IS CORE PYTHON NOT DJANGO STUFF


from django.http import HttpResponse
from django.shortcuts import redirect

# DECORATOR IS A FUNCTION THAT TAKE ANOTHER FUNCTION  AS PARAMETERS
# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
# https://www.python.org/dev/peps/pep-0318/
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print("working: ",  allowed_roles)
            group = None
            if request.user.groups.exists():
                # https://docs.djangoproject.com/en/3.1/topics/auth/default/#permissions-and-authorization
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("you are not authorised")
        return wrapper_func
    return decorator
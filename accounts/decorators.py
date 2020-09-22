# THIS IS CORE PYTHON NOT DJANGO STUFF


from django.http import HttpResponse
from django.shortcuts import redirect

# DECORATOR IS A FUNCTION THAT TAKE ANOTHER FUNCTION  AS PARAMETERS
# https://www.python.org/dev/peps/pep-0318/
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
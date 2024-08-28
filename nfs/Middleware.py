# ***********Authenicated*************
from django.shortcuts import  redirect 

def auth(view_Function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('Login')
        return view_Function(request, *args, **kwargs)
    return wrapped_view


def guest(view_Function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_Function(request, *args, **kwargs)
    return wrapped_view
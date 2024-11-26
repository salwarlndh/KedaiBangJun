from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def kasir_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You must signed in as cashier to access this page.')
                return redirect('sign-in')
        return _wrapped_view
    return decorator
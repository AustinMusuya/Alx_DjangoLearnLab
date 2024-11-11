from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile


def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role


@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

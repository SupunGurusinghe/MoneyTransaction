from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Signup form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "facility_name",
            "phone_num1",
            "phone_num2",
            "address",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "facility_name",
            "phone_num1",
            "phone_num2",
            "address",
        )

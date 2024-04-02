from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "username",
        "email",
        "facility_name",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "facility_name",
                    "phone_num1",
                    "phone_num2",
                    "address",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "facility_name",
                    "email",
                    "username",
                    "password1",
                    "password2",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)

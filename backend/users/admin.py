from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreateForm


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    list_display = ('id', 'username', 'role')
    list_filter = ('role', )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'role'),
            },
        ),
    )
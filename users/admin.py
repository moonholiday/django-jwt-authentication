from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'email', 'phone_number',
                    'photo', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['email', 'phone_number']
    ordering = ['id']


admin.site.register(CustomUser, CustomUserAdmin)

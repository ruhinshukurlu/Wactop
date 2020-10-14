from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_organizer',
            'is_user',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('username','email', 'id', 'is_staff','is_user','is_organizer',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_user','is_organizer')
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ('groups', 'user_permissions',)

    


admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserTB

class UserTBAdmin(UserAdmin):
    model = UserTB
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_active', 'is_staff', 'role', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)

    list_per_page = 20
    fieldsets = (
        ('Personal Info', {
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'phone_number', 'role')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
            'fields': ('created_at',)
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'phone_number', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'
    created_at.short_description = 'Account Created'

admin.site.register(UserTB, UserTBAdmin)

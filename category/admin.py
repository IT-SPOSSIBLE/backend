from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Category
from api.models import UserTB

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name', 'created_by', 'created_at', 'created_by_username', 'action_buttons'
    )
    list_filter = ('created_at', 'created_by')
    search_fields = ('category_name', 'created_by__username')
    ordering = ('-created_at',)
    list_per_page = 20

    fieldsets = (
        ('Category Details', {
            'fields': ('category_name', 'created_by')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

    def created_by_username(self, obj):
        return obj.created_by.email if obj.created_by else "-"
    created_by_username.short_description = 'Created By'

    def action_buttons(self, obj):
        change_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.pk])
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="margin-right: 10px;">✏️ Edit</a>'
            '<a class="button" href="{}" style="color:red;">🗑️ Delete</a>',
            change_url,
            delete_url
        )
    action_buttons.short_description = 'Actions'

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Conversation
from product.models import Product
from api.models import UserTB

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        'moto', 'buyer', 'status', 'started_at', 'conversation_status', 'action_buttons'
    )
    list_filter = ('status', 'started_at')
    search_fields = ('moto__title', 'buyer__username')
    ordering = ('-started_at',)
    list_per_page = 20

    fieldsets = (
        ('Conversation Details', {
            'fields': ('moto', 'buyer', 'status')
        }),
        ('Metadata', {
            'fields': ('started_at',)
        }),
    )

    def conversation_status(self, obj):
        return obj.get_status_display()
    conversation_status.short_description = 'Status'

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

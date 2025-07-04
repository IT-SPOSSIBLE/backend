from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Message
from api.models import UserTB
from conversation.models import Conversation

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'conversation', 'sender_id', 'message_preview', 'sent_at', 'action_buttons'
    )
    list_filter = ('sent_at', 'conversation')
    search_fields = ('conversation__id', 'sender_id__username', 'message_description')
    readonly_fields = ('sent_at',)
    ordering = ('-sent_at',)
    list_per_page = 20

    fieldsets = (
        ('Message Details', {
            'fields': ('conversation', 'sender_id', 'message_description')
        }),
        ('Metadata', {
            'fields': ('sent_at',)
        }),
    )

    def message_preview(self, obj):
        return format_html('<span>{}</span>', obj.message_description[:50] + "...")
    message_preview.short_description = 'Message Preview'

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

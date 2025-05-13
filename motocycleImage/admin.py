from django.contrib import admin
from .models import MotocycleImage
from product.models import Product
from django.utils.html import format_html

@admin.register(MotocycleImage)
class MotocycleImageAdmin(admin.ModelAdmin):
    list_display = ('moto', 'image_preview', 'is_primary', 'uploaded_at')
    list_filter = ('is_primary', 'uploaded_at')
    search_fields = ('moto__title', 'imageUrl')
    readonly_fields = ('uploaded_at',)
    ordering = ('-uploaded_at',)


    list_per_page = 20  
    fieldsets = (
        ('Motocycle Image Details', {
            'fields': ('moto', 'imageUrl', 'is_primary')
        }),
        ('Metadata', {
            'fields': ('uploaded_at',)
        }),
    )

    def image_preview(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.imageUrl)
    image_preview.short_description = 'Image Preview'

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)

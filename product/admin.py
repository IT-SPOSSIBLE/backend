from django.contrib import admin
from .models import Product
from category.models import Category
from motocycleImage.models import MotocycleImage
from api.models import UserTB
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'status', 'posted_by', 'created_at', 'image_preview', 'action_buttons')
    list_filter = ('status', 'category')
    search_fields = ('title', 'posted_by__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 20  

    fieldsets = (
        ('Product Details', {
            'fields': ('title', 'price', 'status')
        }),
        ('Relations', {
            'fields': ('category', 'motocycleImage', 'posted_by')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

    def image_preview(self, obj):
        if obj.motocycleImage and obj.motocycleImage.image:
            return format_html('<img src="{}" style="height: 80px;" />', obj.motocycleImage.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

    def action_buttons(self, obj):
        edit_url = reverse('admin:product_product_change', args=[obj.pk])
        delete_url = reverse('admin:product_product_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="margin-right: 10px;">Edit</a>'
            '<a class="button" href="{}" style="color:red;">Delete</a>',
            edit_url, delete_url
        )
    action_buttons.short_description = 'Actions'
    action_buttons.allow_tags = True

    class Media:
        css = {
            'all': ('grappelli/css/grappelli.css',)
        }
        js = ('grappelli/js/grappelli.js',)

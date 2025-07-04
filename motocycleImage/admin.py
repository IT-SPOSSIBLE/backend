from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import MotocycleImage

@admin.register(MotocycleImage)
class MotocycleImageAdmin(admin.ModelAdmin):
    list_display = (
        'get_title', 'get_price', 'get_category', 'get_status', 'get_posted_by', 
        'image_path', 'image_preview', 'action_buttons',
    )
    list_per_page = 20

    readonly_fields = ('uploaded_at',)

    fieldsets = (
        ('Motocycle Image Details', {
            'fields': ('product', 'image', 'is_primary')
        }),
    )

    def get_title(self, obj):
        return obj.product.title if obj.product else "-"
    get_title.short_description = 'Title'

    def get_price(self, obj):
        return obj.product.price if obj.product else "-"
    get_price.short_description = 'Price'

    def get_category(self, obj):
        return obj.product.category.category_name if obj.product and obj.product.category else "-"
    get_category.short_description = 'Category'

    def get_status(self, obj):
        return obj.product.status if obj.product else "-"
    get_status.short_description = 'Status'

    def get_posted_by(self, obj):
        return obj.product.posted_by if obj.product else "-"
    get_posted_by.short_description = 'Posted By'

    def image_path(self, obj):
        return obj.image.name if obj.image else "No Image"
    image_path.short_description = 'Image Path'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image Preview"

    def action_buttons(self, obj):
        change_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.pk])
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="margin-right: 10px;">✏️ Edit</a>'
            '<a class="button" href="{}" style="color:red;">🗑️ Delete</a>',
            change_url,
            delete_url
        )
    action_buttons.short_description = "Actions"

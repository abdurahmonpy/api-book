from django.contrib import admin
from django.utils.html import format_html
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'display_image', 'pdf', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'slug', 'author')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    display_image.short_description = "Muqova rasmi"

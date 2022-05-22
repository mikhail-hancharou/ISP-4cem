from django.contrib import admin

# Register your models here.
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('id', 'title', 'time_create', 'author')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

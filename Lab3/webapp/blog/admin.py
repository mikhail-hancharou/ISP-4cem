from django.contrib import admin

# Register your models here.
from .models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('id', 'title', 'time_create', 'author', 'photo')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('content', 'author')
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

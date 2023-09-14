from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description', 'url', 'addDate')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('postId', 'title', 'content')
    search_fields = ('title',)
    list_filter = ('catId',)


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

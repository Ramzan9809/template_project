from django.contrib import admin
from ..apps.post.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'image',
        'like',
        'text',
        'created_at',
        'updated_at'
    ]






from django.contrib import admin
from .models import Category, Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'description',
        'price',
        'rating',
        'image', 
        'is_sold', 
        'created_by', 
        'created_at',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
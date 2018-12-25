from django.contrib import admin
from .models import Category, Product, market

@admin.register(market)
class marketAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','activityTXT','countTXT','image','score','addressTXT','description','available']
    list_filter = ['available']
    list_editable = ['score', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
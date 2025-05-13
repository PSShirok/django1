from django.contrib import admin
from .models import Product,Category

@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'first_name')

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('first_name', 'description')






# Register your models here.

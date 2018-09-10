from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description', ]
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)
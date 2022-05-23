from django.contrib import admin
from .models import Update,Contact,Countries,Product,Category


# Register your models here.


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
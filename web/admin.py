from django.contrib import admin
from .models import Update,Contact


# Register your models here.


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
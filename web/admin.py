from django.contrib import admin
from .models import Update,Contact,Countries,Product,Category
from django.utils.safestring import mark_safe

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
    list_display = ( 'category','get_countries','pricelist',)
    def get_queryset(self, request):
        self.full_path = request.get_full_path()
        return super().get_queryset(request)
    def pricelist(self,obj):
        a = '''<a href=" url 'preview-pdf' id={self.id} , name={fdg}>"hji</a>'''
        return mark_safe(a)

    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
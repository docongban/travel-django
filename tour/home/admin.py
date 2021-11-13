from django.contrib import admin
from . models import Category, Product, Customer_Comment
from django_summernote.admin import SummernoteModelAdmin
# from .models import Product


# Register your models here.
admin.site.register(Category) 
# admin.site.register(Product) 

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Product, SomeModelAdmin)

admin.site.register(Customer_Comment)
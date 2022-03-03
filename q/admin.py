from django.contrib import admin
from q.models import *

# Register your models here.


class Contact_Model_Admin(admin.ModelAdmin):
    list_display=['id','username','email','phone','desc']
    
admin.site.register(Contact_Model,Contact_Model_Admin)


class Category_Admin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category, Category_Admin)


class Product_Admin(admin.ModelAdmin):
    list_display = ['id','category','role','name','gender','email','phone','city','description','image']

admin.site.register(Product,Product_Admin)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register_Model(User):
    reemail = models.EmailField(max_length=254)
    repassword = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name


class Contact_Model(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    phone = models.BigIntegerField()
    desc = models.CharField(max_length=4141)



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def all_cat():
        return Category.objects.all()



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    role = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    city = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='imgs/')

    @staticmethod
    def all_pro():
        return Product.objects.all()

    @staticmethod
    def all_with_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.all_pro()
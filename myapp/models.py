from django.db import models
import datetime

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/slider/')
    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name
    

class About(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/about/')

    def __str__(self):
        return self.title
    


    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/blog/')

    def __str__(self):
        return self.title
    




# Create your models here.

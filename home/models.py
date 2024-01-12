from django.db import models
from django.utils.html import format_html

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='drinks')
    detail = models.TextField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/drinks')

    def __str__(self):
        return f'{self.name}-- {self.price}$'

    def images(self):
        return format_html(f"<img src='{self.image.url}' width='30px' height='30px'> ")


class About(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/about')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=85)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.name} : {self.message[:50]}'



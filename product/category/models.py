from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/%Y/%m/%d')
    description=models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name
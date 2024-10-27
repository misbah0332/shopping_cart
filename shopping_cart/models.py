from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return self.title

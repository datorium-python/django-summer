from django.conf import settings
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=250)
    description = models.TextField()

    image = models.ImageField(upload_to='products/')

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(
        to='Category',
    )

    def __str__(self):
        return f'Product: {self.name} belongs to {self.user.email}'


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    products = models.ManyToManyField(
        to=Product,
    )

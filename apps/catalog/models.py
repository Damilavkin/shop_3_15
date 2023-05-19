from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    chosen = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

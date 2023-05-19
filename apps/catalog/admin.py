from mptt.admin import MPTTModelAdmin

from django.contrib import admin

from apps.catalog.models import Category, Product, Image

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Image)

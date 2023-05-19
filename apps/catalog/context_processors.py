from apps.cart.cart import Cart
from apps.catalog.models import Category


def get_shop_context(request):
    return {
        'categories': Category.objects.all(),
        'cart': Cart(request)
    }
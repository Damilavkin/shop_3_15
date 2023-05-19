from copy import deepcopy
from decimal import Decimal

from apps.catalog.models import Product


class Cart:

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        copy_cart = deepcopy(self.cart)
        for product in products:
            copy_cart[str(product.id)]['product'] = product

        for item in copy_cart.values():
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """

        :return:
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        ...
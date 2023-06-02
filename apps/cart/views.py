from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from apps.accounts.forms import OrderCreateForm
from apps.accounts.models import OrderItem
from apps.cart.cart import Cart
from apps.catalog.models import Product


def cart(request, product_id=None):
    form = OrderCreateForm
    cart = Cart(request)
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        cart.add(product)
    return render(request, 'cart/cart.html', {'form': form})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.add(product)
    return HttpResponseRedirect("/cart")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return HttpResponseRedirect("/cart")


def cart_clear(request, product_id=None):
    cart = Cart(request)
    cart.clear()
    return HttpResponseRedirect("/cart")


@login_required
def order(request):
    if request.method == 'POST':
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart_clear(request)
            return render(request,'cart/order.html', {'order': order})
        else:
            return render(request, 'cart/cart.html', {'form': form})
    else:
            return HttpResponseRedirect('/cart')
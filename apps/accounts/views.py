from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView

from apps.accounts.forms import RegisterForm
from apps.accounts.models import Order


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/registration.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@login_required
def dashboard(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'accounts/dashboard.html', {'orders': orders})



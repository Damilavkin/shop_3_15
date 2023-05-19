from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.models import User

from apps.accounts.models import Order


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, *args, **kwargs):
        self.instance.email = self.cleaned_data["email"]
        super().save(*args, **kwargs)
        send_mail(
            subject='Подтверждение регистрации',
            message='Вы зарегестрированы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.instance.email],
            fail_silently=True,
        )


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'phone']
        labels = {'address': 'Адрес', 'phone': 'Телефон'}
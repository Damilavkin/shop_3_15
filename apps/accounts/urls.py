from django.urls import path
from apps.accounts import views

app_name = "accounts"
urlpatterns = [
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('registration', views.RegisterFormView.as_view(), name='registration'),
    path('dashboard', views.dashboard, name='dashboard')
]
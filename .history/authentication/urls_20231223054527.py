from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("user_logout", views.user_logout, name="logout"),
    path("account_locked", views.account_locked, name="account_locked"),
]

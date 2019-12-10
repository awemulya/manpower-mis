from django.urls import path
from . import views

urlpatterns = [
    path('new-passport', views.passport_new, name="new-passport"),
    path('', views.user_login, name="user_login"),
    path('dashboard', views.dashboard, name="dashboard")
]
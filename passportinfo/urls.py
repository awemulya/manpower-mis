from django.urls import path
from . import views

urlpatterns = [
    path('new-passport', views.passport_new, name="new-passport"),
    path('login', views.user_login, name="user_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('info', views.InfoListView.as_view(), name="info-view")
]
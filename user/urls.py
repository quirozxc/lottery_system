from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('password-change/', views.password_change, name='password_change'),
    path('password/<int:seller>/reset/', views.reset_password, name='reset_password'),
    path('seller/create/', views.create_seller, name='create_seller'),
    path('seller/list/', views.list_seller, name='list_seller'),
    path('seller/<int:seller>/change/', views.change_seller, name='change_seller'),
]
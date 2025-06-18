from django.urls import path
from . import views

urlpatterns = [
    path('post/new', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('tienda/', views.tienda, name='tienda'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]
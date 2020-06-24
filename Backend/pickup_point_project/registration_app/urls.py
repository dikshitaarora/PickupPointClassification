from django.urls import path
from . import views

urlpatterns = [
    path('', views.register ,name='register'),
    path('registered/', views.registered ,name='registered'),
    path('registrationframe/', views.frame, name='frame'),
]

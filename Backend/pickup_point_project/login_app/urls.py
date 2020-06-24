from django.urls import path
from login_app import views

urlpatterns = [
	path('', views.login ,name='login'),
	path('login/', views.checkUser ,name='checkUser'),
	path('homepage/', views.homepage ,name='homepage'),
]

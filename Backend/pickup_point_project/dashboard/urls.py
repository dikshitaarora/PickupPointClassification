from django.urls import path
from dashboard import views

urlpatterns = [
	path('',views.index,name='index'),
	# url(r'^$',views.login,name='login'),
	# url(r'^$',views.signup,name='signup'),
]

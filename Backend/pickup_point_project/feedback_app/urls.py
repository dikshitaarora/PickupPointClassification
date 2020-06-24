from django.urls import path
from feedback_app import views

urlpatterns = [
	path('classify/', views.call_model),
]

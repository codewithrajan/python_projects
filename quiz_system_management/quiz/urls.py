from django.urls import path
from django.urls import include
import quiz.views as quiz_views

urlpatterns = [
	path('', quiz_views.qpage),
	
]

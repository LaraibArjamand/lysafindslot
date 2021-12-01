from django.urls import path
from . import views

urlpatterns = [
	path('calendar/find_slot', views.find_slot, name='find_slot'),
]
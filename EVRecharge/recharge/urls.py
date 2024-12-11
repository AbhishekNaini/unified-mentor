from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:station_id>/', views.book_slot, name='book_slot'),
]

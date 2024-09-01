from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_medicine, name='add_medicine'),
    path('search/', views.search_medicine, name='search_medicine'),
    path('scan/', views.scan_medicine, name='scan_medicine'),  # Add this URL
]

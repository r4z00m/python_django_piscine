from . import views
from django.urls import path

urlpatterns = [
    path('init/', views.db_init),
    path('populate/', views.populate),
    path('display/', views.display),
]

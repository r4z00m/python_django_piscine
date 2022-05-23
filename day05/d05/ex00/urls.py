from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.db_init, name='init'),
]

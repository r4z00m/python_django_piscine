from . import views
from django.urls import path

urlpatterns = [
    path('populate/', views.populate),
    path('display/', views.DisplayView.as_view()),
    path('remove/', views.RemoveView.as_view(), name='remove'),
]

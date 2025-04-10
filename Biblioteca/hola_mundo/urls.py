from django.urls import path
from . import views

urlpatterns = [
    path('mundo/', views.hola_mundo),
]
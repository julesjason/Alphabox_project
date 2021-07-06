from django.urls import path
from . import views

urlpatterns= [
    path('', views.config1, name="config1"),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.part, name='part1'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.connection, name='connection'),
]
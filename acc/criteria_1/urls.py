from django.urls import path
from .views import render_temp

urlpatterns = [
    path('temp/', render_temp)
]
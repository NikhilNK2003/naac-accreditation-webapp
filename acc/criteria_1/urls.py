from django.urls import path
from .views import *

urlpatterns = [
    path('temp/', render_temp),
    path('1_2_2/', criteria_1_2_2, name='criteria_1_2_2'),
    path('1_2_2/form/', criteria_1_2_2_form, name='criteria_1_2_2_form'),
]
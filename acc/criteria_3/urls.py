from django.urls import path
from .views import *

urlpatterns = [
    path('3_1_1/', criteria_3_1_1, name='criteria_3_1_1'),
    path('3_1_1/form/', criteria_3_1_1_form, name='criteria_3_1_1_form'),
    path('3_1_1/upload_excel/', upload_excel_3_1_1, name='upload_excel_3_1_1'),
    path('3_1_1/export_excel/', export_excel_3_1_1, name='export_excel_3_1_1'),
    path('3_2_2/', criteria_3_2_2, name='criteria_3_2_2'),
]
from django.shortcuts import render, HttpResponse, redirect
from .models import Criteria_3_1_1
from.forms import *
from datetime import datetime
from django.db import transaction
import openpyxl
from openpyxl import Workbook
from io import BytesIO
from django.contrib import messages
from openpyxl.styles import Alignment, Border, Side, Font, PatternFill
from openpyxl.utils import get_column_letter
# Create your views here.


def criteria_3_1_1(request):
    context = {
        'records' : Criteria_3_1_1.objects.all()
    }
    return render(request, 'table/criteria_3_1_1.html', context=context)

def criteria_3_1_1_form(request):
    pass

def upload_excel_3_1_1(request):
    pass

def export_excel_3_1_1(request):
    pass
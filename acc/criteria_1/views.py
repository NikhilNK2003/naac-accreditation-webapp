from django.shortcuts import render, HttpResponse, redirect
from .models import Criteria_1_2_2
from.forms import *
from datetime import datetime
import openpyxl
from django.contrib import messages
# Create your views here.


def render_temp(request):
    return render(request, 'form/criteria_1_2_2.html')


def criteria_1_2_2(request):
    context = {
        '2021_records': Criteria_1_2_2.objects.filter(year = '2021'),
        '2022_records': Criteria_1_2_2.objects.filter(year = '2022'),
        '2023_records': Criteria_1_2_2.objects.filter(year = '2023'),
        '2024_records': Criteria_1_2_2.objects.filter(year = '2024'),
        '2025_records': Criteria_1_2_2.objects.filter(year = '2025')
    }
    return render(request, 'table/criteria_1_2_2.html', context=context)

def criteria_1_2_2_form(request):
    if request.method == 'POST':
        form = CriteriaForm_1_2_2(request.POST)
        if form.is_valid():
            print(type(form.data))
            form.save() 
            messages.success(request, 'Data Added Successfully')
            return redirect('criteria_1_2_2')
        else:
            messages.error(request, 'Enter valid Data')
    form = CriteriaForm_1_2_2()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_1_2_2.html', context=context)

def upload_excel_1_2_2(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            year = row[0]
            course_name = row[1]
            course_code = row[2]
            year_of_study = row[3]
            period_from = row[4]  
            period_to = row[5]  
            duration = row[6]
            students_enrolled = row[7]
            students_completed = row[8]

            Criteria_1_2_2.objects.create(
                year=year,
                course_name=course_name,
                course_code=course_code,
                year_of_study=year_of_study,
                period_from=period_from,
                period_to=period_to,
                duration=duration,
                students_enrolled=students_enrolled,
                students_completed=students_completed,
            )
        messages.success(request, 'Excel File add Successfully')
        return redirect('criteria_1_2_2')
    messages.error(request, 'Upload valid Excel file')
    return redirect('criteria_1_2_2')
from django.shortcuts import render, redirect
from .models import Criteria_1_2_2
from.forms import *
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
        # year = request.POST.get('year')
        # course_name = request.POST.get('course_name')
        # course_code = request.POST.get('course_code')
        # year_of_study = request.POST.get('year_of_study')
        # from_date = request.POST.get('from_date')
        # to_date = request.POST.get('to_date')
        # course_duration = request.POST.get('course_duration')
        # students_enrolled = request.POST.get('students_enrolled')
        # students_compleated = request.POST.get('students_compleated')
        form = CriteriaForm_1_2_2(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the model if it's valid
            return redirect('criteria_1_2_2')
    form = CriteriaForm_1_2_2()
    context = {
        'form': form,
    }
    return render(request, 'form/criteria_1_2_2.html', context=context)
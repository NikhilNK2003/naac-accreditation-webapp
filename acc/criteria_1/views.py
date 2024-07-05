from django.shortcuts import render

# Create your views here.


def render_temp(request):
    return render(request, 'form/criteria_1_2_2.html')


def criteria_1_2_2(request):
    return render(request, 'table/criteria_1_2_2.html')

def criteria_1_2_2_form(request):
    return render(request, 'form/criteria_1_2_2.html')
from django.shortcuts import render

# Create your views here.


def render_temp(request):
    return render(request, 'base.html')
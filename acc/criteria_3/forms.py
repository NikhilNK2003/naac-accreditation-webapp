from django import forms
from .models import *

class CriteriaForm_3_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_1_1
        fields = [ 'project_name', 'principal_investigator', 'department', 'year_of_award', 'amount_sanctioned', 'duration', 'funding_agency', 
    'grant_type' ]
        widgets = {
            'grant_type': forms.Select(attrs={'class': 'form-select'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Name'}),
            'principal_investigator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Principal Investigator'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Duration'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'year_of_award': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Award'}),
            'amount_sanctioned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount Sanctioned'}),
            'funding_agency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Funding Agency'}),
        }



class CriteriaForm_3_2_2(forms.ModelForm):
    class Meta:
        model = Criteria_3_2_2
        fields = [ 'year', 'event_name', 'num_participants', 'date_from', 'date_to', 'activity_report_link' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Event Name'}),
            'num_participants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Participants'}),
            'date_from': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'date_to': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'activity_report_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Link '}),
        }

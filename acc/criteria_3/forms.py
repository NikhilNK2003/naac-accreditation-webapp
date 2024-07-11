from django import forms
from .models import *

class CriteriaForm_3_1_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_1_1
        fields = ['year', 'project_name', 'principal_investigator', 'department', 'year_of_award', 'amount_sanctioned', 'duration', 'funding_agency', 
    'grant_type' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'grant_type': forms.Select(attrs={'class': 'form-select'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project Name'}),
            'principal_investigator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Principal Investigator'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Duration'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
            'year_of_award': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year of Award'}),
            'amount_sanctioned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount Sanctioned'}),
            'funding_agency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Funding Agency'}),
        }


class CriteriaForm_3_5_1(forms.ModelForm):
    class Meta:
        model = Criteria_3_5_1
        fields = ['year', 'mou_name', 'institution_name', 'signing_year', 'pourpose', 'duration', 'activities', 
    'document_link' ]
        widgets = {
            'year': forms.Select(attrs={'class': 'form-select'}),
            'mou_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter MOU Name'}),
            'institution_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Name'}),
            'signing_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Signing Year'}),
            'pourpose': forms.Select(attrs={'class': 'form-select'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Duration'}),
            'activities': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Activities'}),
            'document_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Document Link'}),
        }

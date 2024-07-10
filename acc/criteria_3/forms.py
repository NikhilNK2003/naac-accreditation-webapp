from django import forms
from .models import Criteria_3_1_1

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

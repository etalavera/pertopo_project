from django import forms
from .models import *

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'project_name',
            'project_leader',
            'project_address',
            'project_city',
            'project_seller',
            'project_machine_operator',
            'project_machine',
            'project_custommer',
            'project_start_date',
            'project_estimate_meters',
            'project_price_per_meter',
            'project_observations',
        )
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_leader': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_address': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_city': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_seller': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_machine_operator': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_machine': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_custommer': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_start_date': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_estimate_meters': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_price_per_meter': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'project_observations': forms.Textarea(

            attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }

class LogbookForm(forms.ModelForm):
    class Meta:
        model = Logbooks
        fields = (
            'project',
            'log_date',
            'log_task',
            'log_meters',
        )
        widget = {
            'log_date': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'log_task': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'log_meters': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
        }

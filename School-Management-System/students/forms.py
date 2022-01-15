from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-2020'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: LM01'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Steve Smith'}),
            'fathers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3732106814'}),
            'fathers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01884334899'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Steve Smith'}),
            'mothers_nid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3732106814'}),
            'mothers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01884334899'}),
        }


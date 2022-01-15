from django import forms

class OfficialInfoForm(forms.Form):
    official_register_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'LM10'}))
    official_register_date = forms.CharField(widget=forms.DateInput(attrs={'placeholder': '22-07-1990'}))


class PersonalInfo(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    dob = forms.CharField(widget=forms.DateInput(attrs={'placeholder': '22-07-1990'}))
    another_fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    national_id = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': ''}))
    employee_avatar = forms.CharField(widget=forms.FileInput(attrs={'placeholder': ''}))
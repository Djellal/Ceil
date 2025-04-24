from django import forms
from .models import Session, AppSettings

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AppSettingsForm(forms.ModelForm):
    class Meta:
        model = AppSettings
        fields = '__all__'
        widgets = {
            'terms_and_conditions': forms.Textarea(attrs={'rows': 5}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
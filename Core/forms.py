from django import forms
from .models import Session, AppSettings, State, Municipality, Profession, CourseType, Course

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

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'name_ar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
        }

class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ['name', 'name_ar', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'state': forms.HiddenInput(),
        }

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['name', 'name_ar', 'fee_value']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'fee_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class CourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = ['name', 'name_ar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'name_ar', 'duration', 'image', 'course_type', 'is_active']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_ar': forms.TextInput(attrs={'class': 'form-control', 'dir': 'rtl'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_type': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
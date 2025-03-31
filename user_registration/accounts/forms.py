from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'type': 'tel'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
       
        date_of_birth = cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > datetime.date.today():
            raise ValidationError("Date of birth cannot be in the future.")

        
        phone_number = cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        
        return cleaned_data

from django import forms
from django.contrib.auth.models import User
from .models import Author, Quote

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'text']

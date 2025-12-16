from django import forms

class CreateAccountRequestForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)

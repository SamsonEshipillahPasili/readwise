from django import forms

class CreateAccountRequestForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)

    def clean_password(self) -> str:
        password = self.cleaned_data.get('password', '')
        if len(password) < 8:
            raise forms.ValidationError('Password should have a minimum of 8 characters.')
        return password
    
    def clean_confirm_password(self) -> str:
        password = self.cleaned_data.get('password', '')
        confirm_password = self.cleaned_data.get('confirm_password', '')
        
        if password != confirm_password:
            raise forms.ValidationError('The passwords do not match.')
        
        return confirm_password


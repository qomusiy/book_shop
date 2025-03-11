from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class RegisterForm(forms.ModelForm):
    raw_password = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        raw_password = cleaned_data.get('raw_password')
        if password!= raw_password:
            raise forms.ValidationError("Passwords don't match!")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'lebel':'Username', 'class':'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'lebel':'Password', 'class':'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bunday foydalanuvchi mavjud emas')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError("password kiritilmagan")
        return password
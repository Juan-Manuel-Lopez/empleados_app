from django import forms
from django.contrib.auth.models import User
from empleados_app.models import Empleados, UserProfileInfo


class NewEmpForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

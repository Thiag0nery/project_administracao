from django import forms
from . import models
from django.contrib.auth.models import User
class form_pessoa(forms.ModelForm):
    class Meta:
        model = models.pessoa
        fields = '__all__'
        exclude = ('pjuri_cod',)

class form_user(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
    )
    password_repeat = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
    )
    class Meta:
        model = User
        fields = ('first_name', 'email','password','password_repeat',)
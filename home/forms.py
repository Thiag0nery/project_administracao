from django import forms
from . import models

class form_pessoa(forms.ModelForm):
    class Meta:
        model = models.pessoa
        fields = '__all__'
        exclude = ('pjuri_cod',)
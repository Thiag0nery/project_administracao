from django import forms
from . import models
from django.contrib.auth.models import User
from validate_docbr import CPF
from validate_docbr import CNPJ

error_msg_email_exists = 'E-mail já existe'
error_msg_password_match = 'As duas senhas não conferem'
error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracteres'
error_msg_required_field = 'Este campo é obrigatório.'
error_msg_invalid_field = 'Informação invalida'
error_cpf_invalid = 'CPF invalido'
error_cnpj_invalid = 'CNPJ invalido'
error_cpf_exist = 'CPF ja cadastrado no sistema'

cpf = CPF()
cnpj = CNPJ()
class form_pessoa(forms.ModelForm):
    class Meta:
        model = models.pessoa
        fields = '__all__'
        exclude = ('pes_cod','pes_usuario_fk',)
    def clean(self, *args, **kwargs):
        validation_error_msgs = {}
        form_cpf = self.cleaned_data.get('pes_cpf')

        form_cpf = form_cpf.replace('.', '').replace(',', '').replace('-', '').replace('/', '')

        cpf_banco = models.pessoa.objects.filter(pes_cpf=form_cpf).first()

        if cpf_banco:
            validation_error_msgs['pes_cpf'] = error_cpf_exist

        cpf = CPF()
        is_valid = cpf.validate(form_cpf)
        if not is_valid:
            validation_error_msgs['pes_cpf'] = error_cpf_invalid

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
        pass
class form_pessoa_juridica(forms.ModelForm):
    class Meta:
        model = models.pessoa_juridica
        fields = '__all__'
        exclude = ('pjuri_cod','pjuri_usuario_fk',)

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

    def clean(self, *args, **kwargs):
        validation_error_msgs = {}
        email = self.cleaned_data.get('email').lower()
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        email_exists = User.objects.filter(username=email).first()

        if email_exists:
            validation_error_msgs['email'] = error_msg_email_exists

        if password != password_repeat:
            validation_error_msgs['password'] = error_msg_password_match
            validation_error_msgs['password_repeat'] = error_msg_password_match
        if len(password) < 6:
            validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
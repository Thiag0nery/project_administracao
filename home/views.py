from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from . import forms
import random



# LOGIN
class Viem_login(View):
    templates_name = 'home/login.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.templates_name)


# FECHAMENTO LOGIN
# CADASTRO
def View_cadastrar(request):
    templates_name = 'home/cadastro.html'
    context = {
        'usuario': forms.form_user(data=request.POST or None),
        'pessoa': forms.form_pessoa(data=request.POST or None),
        'pessoa_juridica': forms.form_pessoa_juridica(data=request.POST or None)
    }

    return render(request, templates_name, context)
def ajax_email(request):

    try:
        email_requisicao = request.GET.get('email').lower()

        email_validate_pessoa = random.randint(1000, 5000)
        response = HttpResponse("Cookie set!")
        subject = 'Codigo de verificação'
        message = f'Código: {email_validate_pessoa}'

        from_email = 'betateste456@hotmail.com'
        recipient_list = [email_requisicao, ]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        data = {'sucessos_email': f'Email enviado com sucesso! Verrifique a sua caixa de entrada ou Spam'}
        response = JsonResponse(data, safe=False)
        response.set_cookie('email_validate_pessoa', email_validate_pessoa)
        return response
    except:
        print('aqui')
        data = {'error_email': f'Não foi possivel enviar email, verrifique se esta correto o campo!'}
        return JsonResponse(data, safe=False)

def ajax_email_empresa(request):
    try:
        email_requisicao = request.GET.get('email').lower()


        email_validate_empresa = random.randint(1000, 5000)

        response = HttpResponse("Cookie set!")
        #response.set_cookie('email_validate_empresa', email_validate_empresa)

        subject = 'Codigo de verificação'
        message = f'Código: {email_validate_empresa}'
        from_email = 'betateste456@hotmail.com'
        recipient_list = [email_requisicao, ]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        data = {'sucessos_email': f'Email enviado com sucesso! Verrifique a sua caixa de entrada ou Spam'}

        response = JsonResponse(data, safe=False)
        response.set_cookie('email_validate_empresa', email_validate_empresa)
        return response
    except:
        data = {'error_email': f'Não foi possivel enviar email, verrifique se esta correto o campo!'}
        return JsonResponse(data, safe=False)


@csrf_protect
def cadastro_usuario(request):

    if request.method == 'POST':

        tipo_pessoa = request.POST.get('pes_tipo')

        validacao_email_pessoa = request.COOKIES.get('email_validate_pessoa')
        validacao_email_empresa = request.COOKIES.get('email_validate_empresa')
        inp_email_empresa = request.POST.get('input_validacao_email2')
        inp_email_pessoa = request.POST.get('input_validacao_email1')

        form_usuario = forms.form_user(request.POST)
        form_pessoa = forms.form_pessoa(request.POST)
        form_pessoa_juridica = forms.form_pessoa_juridica(request.POST)
        print(int(validacao_email_empresa) ==int(inp_email_empresa))
        print((form_usuario))
        if ((form_usuario.is_valid() and form_pessoa.is_valid() and int(validacao_email_empresa) ==
             int(inp_email_empresa) and form_pessoa_juridica.is_valid() and tipo_pessoa == 'Pessoa Jurídica') and
                int(validacao_email_pessoa) == int(inp_email_pessoa)):
            usuario_banco = form_usuario.save(commit=False)
            usuario_banco.set_password(request.POST.get('password'))
            usuario_banco.username = request.POST.get('email').lower()
            usuario_banco.save()

            banco_pessoa = form_pessoa.save(commit=False)
            banco_pessoa.pes_usuario_fk = usuario_banco
            banco_pessoa.save()

            banco_pessoa_juridica = form_pessoa_juridica.save(commit=False)
            banco_pessoa_juridica.pjuri_usuario_fk = usuario_banco

            return JsonResponse({'success': True})

        if (form_usuario.is_valid() and form_pessoa.is_valid() and int(validacao_email_pessoa) == int(inp_email_pessoa)
                and tipo_pessoa == 'Pessoa Física'):
            usuario_banco = form_usuario.save(commit=False)
            usuario_banco.set_password(request.POST.get('password'))
            usuario_banco.username = request.POST.get('email').lower()
            usuario_banco.save()

            banco_pessoa = form_pessoa.save(commit=False)
            banco_pessoa.pes_usuario_fk = usuario_banco
            banco_pessoa.save()
            return JsonResponse({'success': True})





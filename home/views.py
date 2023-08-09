from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.http import JsonResponse
from . import forms
import random


# Criar o array 3 x 3 com números aleatórios entre 1 e 52

email_validate = None
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
    }

    return render(request, templates_name, context)
def ajax_email(request):
    try:
        email_requisicao = request.GET.get('email').lower()
        email_validate = random.randint(1000, 5000)
        subject = 'Codigo de verificação'
        message = f'Código: {email_validate}'
        from_email = 'betateste456@hotmail.com'
        recipient_list = [email_requisicao, ]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        data = {'sucessos_email': f'Email enviado com sucesso! Verrifique a sua caixa de entrada ou Spam'}
        return JsonResponse(data, safe=False)
    except:
        data = {'error_email': f'Não foi possivel enviar email, verrifique se esta correto o campo!'}
        return JsonResponse(data, safe=False)

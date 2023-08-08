from django.shortcuts import render
from django.views import View

# LOGIN
class Viem_login(View):
    templates_name = 'home/login.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.templates_name)


# FECHAMENTO LOGIN
# CADASTRO
class View_cadastrar(View):
    templates_name = 'home/cadastro.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.templates_name)

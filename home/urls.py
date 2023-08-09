from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.Viem_login.as_view(), name='login'),
    path('Cadastro/', views.View_cadastrar, name='cadastrar'),
    path('email_validade', views.ajax_email, name='email_validade')
]
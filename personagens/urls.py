from django.urls import path
from .views import ProfissoesAPIView, AtributosAPIView, ModificadoresAPIView, PersonagensAPIView, JogoAPIView


urlpatterns = [
    path('profissoes/', ProfissoesAPIView.as_view(), name='profissoes'),
    path('atributos/', AtributosAPIView.as_view(), name='atributos'),
    path('modificadores/', ModificadoresAPIView.as_view(), name='modificadores'),
    path('personagens/', PersonagensAPIView.as_view(), name='nomes'),
    path('jogo/', JogoAPIView.as_view(), name='jogo'),
]

# Usa-se a chave para acessar e poder apagar ou atualizar
# http://localhost:8000/api/v1/profissoes/1/
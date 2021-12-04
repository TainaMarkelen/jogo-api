from .models import Personagens, Atributos, Modificadores
from django.shortcuts import get_object_or_404

class PersonagensDao:
        
    def get_personagem_by_nome(self, nome):
        return get_object_or_404(Personagens, nome=nome)
       
    def get_atributos_by_profissao_id(self, id): 
        atributos: Atributos = get_object_or_404(Atributos, profissoes=id)
        return atributos
        
    def get_modificadores_by_profissao_id(self, id):
        modificadores: Modificadores = get_object_or_404(Modificadores, profissoes=id)
        return modificadores
from rest_framework import serializers
from .models import Profissoes, Atributos, Modificadores, Personagens

        
class AtributosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Atributos
        fields = (
            'profissoes',
            'pontos',
            'forca',
            'destreza',
            'inteligencia'
        )

class ModificadoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Modificadores
        fields = (
            'profissoes',
            'ataque',
            'velocidade'
        )
        
class ProfissoesSerializer(serializers.ModelSerializer):
    atributos = AtributosSerializer(read_only=True)
    modificadores = ModificadoresSerializer(read_only=True)
    
    class Meta:
        model = Profissoes
        fields = (
            'profissoes',
            'atributos',
            'modificadores'
        )
        
class PersonagensSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personagens
        fields = (
            'profissoes',
            'nome'
        )
        

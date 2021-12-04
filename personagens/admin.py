from django.contrib import admin

from .models import Profissoes, Atributos, Modificadores, Personagens

@admin.register(Profissoes)
class ProfissoesAdmin(admin.ModelAdmin):
    list_display = ('profissoes',)
    
@admin.register(Atributos)
class AtributosAdmin(admin.ModelAdmin):
    list_display = ('profissoes',)
    
@admin.register(Modificadores)
class ModificadoresAdmin(admin.ModelAdmin):
    list_display = ('profissoes',)

@admin.register(Personagens)   
class PersonagensAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissoes')
        
    
    
    
    

''' Aqui só serão colocados os dados correspondentes
a administração do site, como a iserção dos atributos
e os nomes dos personagens '''

''' Siga para as views para inserir dados correspondentes
ao usuario, como cadastro de nome '''

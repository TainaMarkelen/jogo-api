from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

          
class Profissoes(Base): 
    profissoes = models.CharField('Profissões', max_length=15)
    
    class Meta:
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'
    
    def __str__(self):
            return self.profissoes


class Atributos(Base):
    profissoes = models.OneToOneField(Profissoes, on_delete=models.CASCADE)
    pontos = models.IntegerField('Pontos de Vida')
    forca = models.IntegerField('Força')
    destreza = models.IntegerField('Destreza')
    inteligencia = models.IntegerField('Inteligência')
    
    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'
         
    def __Profissao__(self):
        return self.profissoes
 
       
class Modificadores(Base):
    profissoes = models.OneToOneField(Profissoes, on_delete=models.CASCADE)
    ataque = models.IntegerField('Ataque')
    velocidade = models.IntegerField('Velocidade')
    
    class Meta:
        verbose_name = 'Modificador de batalha'
        verbose_name_plural = 'Modificadores de batalha'
    
    def __Profissao__(self):
        return self.profissoes
    
    
class Personagens(Base):
    profissoes = models.ForeignKey(Profissoes, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=15, unique=True)
    
    class Meta:
        verbose_name = 'Nome'
        verbose_name_plural = 'Nomes'

    
    
    

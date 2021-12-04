import pytest
import unittest
from unittest import mock
from unittest.mock import MagicMock
from jogo.wsgi import *
from personagens.jogo_service import JogoService
from personagens.random_service import RandomService
from personagens.personagens_dao import PersonagensDao
from setuptools._vendor.more_itertools.more import side_effect
from personagens.models import Personagens, Atributos, Modificadores, Profissoes

class TestJogoService(unittest.TestCase):

    def setUp(self):
        self.random_service = MagicMock(autospec=RandomService)
        self.personagens_dao = MagicMock(autospec=PersonagensDao)
        self.jogo_service = JogoService(self.random_service, self.personagens_dao)
        
    def test_fight(self):
        self.random_service.get_random_number.side_effect = self.get_random_number_side_effect
        
        self.personagens_dao.get_personagem_by_nome.side_effect = self.get_personagem_by_nome_side_effect
        self.personagens_dao.get_atributos_by_profissao_id.side_effect = self.get_atributos_by_profissao_id_side_effect
        self.personagens_dao.get_modificadores_by_profissao_id.side_effect = self.get_modificadores_by_profissao_id_side_effect
        
        winner = self.jogo_service.fight({"name1": "Ana", "name2": "Maria"})
        
        self.assertEqual("Maria", winner)
        
    def get_profissao(self, id):
        profissao = Profissoes()
        profissao.pk = id
        return profissao
        
    def get_personagem_by_nome_side_effect(self, nome):
        personagem = Personagens()
        personagem.nome = nome
        if nome == "Ana": 
            personagem.profissoes = self.get_profissao(1)
        else:
            personagem.profissoes = self.get_profissao(2)
        return personagem
    
    def get_atributos_by_profissao_id_side_effect(self, id):
        atributos = Atributos()
        atributos.profissoes = self.get_profissao(id)
        if id == 1:
            atributos.pontos = 10
        else:
            atributos.pontos = 20
        return atributos
            
    def get_modificadores_by_profissao_id_side_effect(self, id):
        modificadores = Modificadores()
        modificadores.profissoes = self.get_profissao(id)
        if id == 1:
            modificadores.ataque = 2
            modificadores.velocidade = 3
            
        else:
            modificadores.ataque = 11
            modificadores.velocidade = 12
        return modificadores
        
    def get_random_number_side_effect(self, min, max):
        if min == 0:
            if max == 3:
                return 1
            elif max == 12:
                return 10
            else:
                return 11
        else:
            return 0    
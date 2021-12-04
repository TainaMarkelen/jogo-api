from .models import Personagens, Atributos, Modificadores
from personagens.random_service import RandomService
from personagens.personagens_dao import PersonagensDao

class JogoService:
    def __init__(self, random_service: RandomService, personagens_dao: PersonagensDao):
        self.random_service = random_service
        self.personagens_dao = personagens_dao
    
    def fight(self, fight_request):
        #print(fight_request)
        calc_vel1 = 0
        calc_vel2 = 0
        
        personagem1 = self.personagens_dao.get_personagem_by_nome(fight_request["name1"])
        personagem2 = self.personagens_dao.get_personagem_by_nome(fight_request["name2"])
        
        modificadores1 = self.personagens_dao.get_modificadores_by_profissao_id(personagem1.profissoes.pk)
        modificadores2 = self.personagens_dao.get_modificadores_by_profissao_id(personagem2.profissoes.pk)
        
        atributos1 = self.personagens_dao.get_atributos_by_profissao_id(personagem1.profissoes.pk)
        atributos2 = self.personagens_dao.get_atributos_by_profissao_id(personagem2.profissoes.pk)
          
        while calc_vel1 == calc_vel2:
            calc_vel1 = self.random_service.get_random_number(0, modificadores1.velocidade) # Personagem1
            print(calc_vel1)
     
            calc_vel2 = self.random_service.get_random_number(0, modificadores2.velocidade) #personagem2
            print(calc_vel2)
             
            if calc_vel1 > calc_vel2:
                print (f'{personagem1.nome} foi mais veloz que {personagem2.nome} e irá começar!')
                return self.partida(personagem1,personagem2, modificadores1, modificadores2, atributos1, atributos2)
            elif calc_vel2 > calc_vel1:              
                print (f'{personagem2.nome} foi mais veloz que {personagem1.nome} e irá começar!')
                return self.partida(personagem2, personagem1, modificadores2, modificadores1, atributos2, atributos1) 
        
    def partida(self, attacking_character: Personagens, defending_character: Personagens, attacking_modifiers: Modificadores, defending_modifiers: Modificadores, attacking_attributes: Atributos, defending_attributes: Atributos):
        calc_ataque = self.random_service.get_random_number(0, attacking_modifiers.ataque)
        defending_attributes.pontos -= calc_ataque
        print (f'{attacking_character.nome} atacou {defending_character.nome} com {calc_ataque} de dano, {defending_character.nome} com {defending_attributes.pontos} de vidas restantes;')
        
        if defending_attributes.pontos <= 0:
            print(f'{attacking_character.nome} venceu')
            return attacking_character.nome 
        else:
            return self.partida(defending_character, attacking_character, defending_modifiers, attacking_modifiers, defending_attributes, attacking_attributes)
        
            
            
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Profissoes, Atributos, Modificadores, Personagens
from .serializers import ProfissoesSerializer, AtributosSerializer, ModificadoresSerializer, PersonagensSerializer

from .jogo_service import JogoService
from personagens.random_service import RandomService
from personagens.personagens_dao import PersonagensDao

class ProfissoesAPIView(APIView):
    
    def get(self, request):
        profissoes = Profissoes.objects.all()
        serializer = ProfissoesSerializer(profissoes, many=True)
        return Response(serializer.data)
    
    
class AtributosAPIView(APIView):
    
    def get(self, request):
        atributos = Atributos.objects.all()
        serializer = AtributosSerializer(atributos, many=True)
        return Response(serializer.data)
    
    
class ModificadoresAPIView(APIView):
    
    def get(self, request):
        modificadores = Modificadores.objects.all()
        serializer = ModificadoresSerializer(modificadores, many=True)
        return Response(serializer.data)
    
 
class PersonagensAPIView(APIView):
    def get(self, request):
        personagens = Personagens.objects.all()
        serializer = PersonagensSerializer(personagens, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonagensSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class JogoAPIView(APIView):

    def __init__(self):
        random_service = RandomService()
        personagens_dao = PersonagensDao()
        self.jogo_service = JogoService(random_service, personagens_dao)
        
    def post(self, request):
        fight_request = request.data
        result = self.jogo_service.fight(fight_request)
        
        return Response({"winner": result}, status=status.HTTP_201_CREATED)


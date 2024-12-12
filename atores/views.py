from rest_framework import generics
from atores.models import Ator
from atores.serializers import ActorSerializer


#essas views herdam classes de generics do drf para criar e listar itens
class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = ActorSerializer
    

#essas views herdam classes de generics do drf para alterar, deletar e buscar por itens especificos    
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = ActorSerializer
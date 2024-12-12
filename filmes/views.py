from rest_framework import generics
from filmes.models import Filme
from filmes.serializers import FilmeSerializer

class FilmeCreateListView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
    
class FilmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()    
    serializer_class = FilmeSerializer 
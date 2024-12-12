from rest_framework import generics
from generos.models import Genero
from generos.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer
        
        

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from generos.models import Genero
from generos.serializers import GenreSerializer
from generos.permissions import GenrePermissionsClass

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionsClass,)
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionsClass,)
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer
        
        

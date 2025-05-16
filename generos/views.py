from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermissions
from generos.models import Genero
from generos.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermissions,
    )
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermissions,
    )
    queryset = Genero.objects.all()
    serializer_class = GenreSerializer

from django.shortcuts import render
from rest_framework import generics
from avaliacoes.models import Avaliacao
from avaliacoes.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = ReviewSerializer

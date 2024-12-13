from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from avaliacoes.models import Avaliacao
from avaliacoes.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = ReviewSerializer

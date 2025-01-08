from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from filmes.models import Filme
from filmes.serializers import FilmeSerializer
from avaliacoes.models import Avaliacao


class FilmeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Filme.objects.all()

    def get(self, request):
        total_moveis = self.queryset.count()
        movies_by_genre = self.queryset.values('genero__nome').annotate(count=Count('id'))
        total_avaliacoes = Avaliacao.objects.count()
        average_stars = Avaliacao.objects.aggregate(avg_estrelas=Avg('estrelas'))['avg_estrelas']

        return response.Response(data={
            'total_moveis': total_moveis,
            'movies_by_genre': movies_by_genre,
            'total_avaliacoes': total_avaliacoes,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }, status=status.HTTP_200_OK)

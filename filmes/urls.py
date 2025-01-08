from django.urls import path
from . import views


urlpatterns = [
    path('filmes/', views.FilmeCreateListView.as_view(), name='filme-create-list'),
    path('filmes/<int:pk>/', views.FilmeRetrieveUpdateDestroyView.as_view(), name='filme-detail-view'),
    path('filmes/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('generos/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('generos/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]

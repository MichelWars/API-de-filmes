from django.urls import path
from . import views

urlpatterns = [

      
    path('filmes/', views.FilmeCreateListView.as_view(), name='filme-create-list'),
    path('filmes/<int:pk>/', views.FilmeRetrieveUpdateDestroyView.as_view(), name='filme-detail-view'), 
    

]
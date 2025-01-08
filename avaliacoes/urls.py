from django.urls import path
from . import views


urlpatterns = [


    path('avaliacoes/', views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('avaliacoes/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),


]

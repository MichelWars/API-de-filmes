from django.urls import path

from . import views

urlpatterns = [
    path(
        'atores/',
        views.ActorCreateListView.as_view(),
        name='actor-create-list',
    ),
    path(
        'atores/<int:pk>/',
        views.ActorRetrieveUpdateDestroyView.as_view(),
        name='actor-detail-view',
    ),
]

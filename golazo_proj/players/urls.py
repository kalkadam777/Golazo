from django.urls import path
from .views import PlayerListView, PlayerDetailView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player-list'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
]
from django.urls import path
from .views import PlayerListView, PlayerDetailView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView, ValuablePlayersList, YoungPlayersListView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player-list'),
    path('valuable/', ValuablePlayersList.as_view(), name='valuable-players-list'),
    path('young/', YoungPlayersListView.as_view(), name='young-player-list'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('create/', PlayerCreateView.as_view(), name='player-create'),
    path('<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),
]
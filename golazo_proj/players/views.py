import logging
from django.shortcuts import render
from .models import Player
from rest_framework import generics
from .serializers import PlayerSerializer
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Настраиваем логгер
logger = logging.getLogger('players')
debug_logger = logging.getLogger('debug_logger')

def home(request):
    try:
        valuable_players = Player.objects.order_by('-value')[:5]
        young_players = Player.objects.order_by('age')[:5]
        logger.info("Accessed home page: valuable and young players listed.")
        debug_logger.debug("Home page data: valuable_players=%s, young_players=%s", valuable_players, young_players)
    except Exception as e:
        logger.error(f"Error retrieving players for home page: {e}")

    context = {
        'valuable_players': valuable_players,
        'young_players': young_players,
    }
    return render(request, 'home.html', context)


class ValuablePlayersList(generics.ListAPIView):
    queryset = Player.objects.order_by('-value')[:5]
    serializer_class = PlayerSerializer

    def list(self, request, *args, **kwargs):
        logger.info("API accessed: List of valuable players.")
        debug_logger.debug("Valuable players queryset: %s", self.queryset)
        return super().list(request, *args, **kwargs)


class YoungPlayersListView(generics.ListAPIView):
    queryset = Player.objects.order_by('age')[:5]
    serializer_class = PlayerSerializer

    def list(self, request, *args, **kwargs):
        logger.info("API accessed: List of young players.")
        debug_logger.debug("Young players queryset: %s", self.queryset)
        return super().list(request, *args, **kwargs)


class PlayerListView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'position': ['exact'],
        'value': ['gte', 'lte'],
    }
    search_fields = ['name', 'position']
    ordering_fields = ['value', 'age', 'name']
    ordering = ['-value']

    def list(self, request, *args, **kwargs):
        logger.info("API accessed: Full player list.")
        debug_logger.debug("Player list filters: %s", request.query_params)
        return super().list(request, *args, **kwargs)


class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        logger.info(f"Player details accessed: {player.name} (ID: {player.id})")
        debug_logger.debug("Player details: %s", player)
        return super().retrieve(request, *args, **kwargs)


class PlayerCreateView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"Attempting to create a new player: {request.data}")
        debug_logger.debug("Create player data: %s", request.data)
        return super().create(request, *args, **kwargs)


class PlayerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def update(self, request, *args, **kwargs):
        player = self.get_object()
        logger.info(f"Player updated: {player.name} (ID: {player.id}). Data: {request.data}")
        debug_logger.debug("Update player data: %s", request.data)
        return super().update(request, *args, **kwargs)


class PlayerDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def destroy(self, request, *args, **kwargs):
        player = self.get_object()
        logger.info(f"Player deleted: {player.name} (ID: {player.id})")
        debug_logger.debug("Deleted player details: %s", player)
        return super().destroy(request, *args, **kwargs)
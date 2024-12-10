from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LeagueViewSet,
    MatchViewSet,
    StandingsViewSet,
    league_list,
    league_detail,
    generate_matches,
    update_standings
)

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet, basename='league')
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'standings', StandingsViewSet, basename='standing')

urlpatterns = [
    path('leagues/list/', league_list, name='league_list'),
    path('leagues/<int:pk>/', league_detail, name='league_detail'),
    path('leagues/<int:pk>/generate-matches/', generate_matches, name='generate_matches'),
    path('leagues/<int:pk>/update-standings/', update_standings, name='update_standings'),
    path('', include(router.urls)),
]
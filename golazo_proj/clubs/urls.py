from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club-list'),
]
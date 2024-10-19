from django.urls import path
from .views import ClubListView, ClubDetailView, ClubCreateView, ClubUpdateView, ClubDeleteView

urlpatterns = [
    path('', ClubListView.as_view(), name='club-list'),
    path('<int:pk>/', ClubDetailView.as_view(), name='club-detail'),
    path('create/', ClubCreateView.as_view(), name='club-create'),
    path('<int:pk>/update/', ClubUpdateView.as_view(), name='club-update'),
    path('<int:pk>/delete/', ClubDeleteView.as_view(), name='club-delete'),
]

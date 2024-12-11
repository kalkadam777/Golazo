from django.urls import path
from .views import BroadcastListView, BroadcastDetailView, BroadcastCreateView, BroadcastUpdateView, BroadcastDeleteView

urlpatterns = [
    path('', BroadcastListView.as_view(), name='broadcast-list'),
    path('<int:pk>/', BroadcastDetailView.as_view(), name='club-detail'),
    path('create/', BroadcastCreateView.as_view(), name='club-create'),
    path('<int:pk>/update/', BroadcastUpdateView.as_view(), name='club-update'),
    path('<int:pk>/delete/', BroadcastDeleteView.as_view(), name='club-delete'),
]

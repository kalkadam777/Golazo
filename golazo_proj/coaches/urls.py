from django.urls import path
from .views import ManagerListView, ManagerDetailView, ManagerCreateView, ManagerUpdateView, ManagerDeleteView

urlpatterns = [
    path('', ManagerListView.as_view(), name='manager-list'),
    path('<int:pk>/', ManagerDetailView.as_view(), name='manager-detail'),
    path('create/', ManagerCreateView.as_view(), name='manager-create'),
    path('<int:pk>/update/', ManagerUpdateView.as_view(), name='manager-update'),
    path('<int:pk>/delete/', ManagerDeleteView.as_view(), name='manager-delete'),
]
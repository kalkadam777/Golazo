from django.urls import path
from .views import RegisterView, CurrentUserView, UserProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('me/', CurrentUserView.as_view(), name='current_user'),                
    path('me/profile/', UserProfileView.as_view(), name='user_profile'),        
]
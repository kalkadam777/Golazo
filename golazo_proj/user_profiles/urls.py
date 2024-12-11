# /Users/lzandaribaev/Desktop/WEB/projects/Golazo/golazo_proj/user_profiles/urls.py
from django.urls import path
from .views import (
    register, user_login, user_logout,
    RegisterView, CurrentUserView, UserProfileView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # HTML template views
    path('register/', register, name='register'),  # Регистрация через шаблон
    path('login/', user_login, name='login'),      # Логин через шаблон
    path('logout/', user_logout, name='logout'),   # Логаут через шаблон

    # API views
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api/me/', CurrentUserView.as_view(), name='current_user'),                
    path('api/me/profile/', UserProfileView.as_view(), name='user_profile'),
]
from django.urls import path
from account.views import ActivationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
    # Регистрация - Айдын
    # Почта + активация - Саян + Адиль
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view())
    # смена пароля - Эркин
]

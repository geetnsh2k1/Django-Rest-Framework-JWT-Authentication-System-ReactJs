from django.urls import path
from .views import logout, google, refresh, signup

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('refresh/token/', TokenRefreshView.as_view(), name="refresh"),
    path('verify/', TokenVerifyView.as_view(), name="verify"),
    path('logout/', logout, name="logout"),
    
    path('refresh/', refresh),
    
    path('google/', google),
    
    path('signup/', signup),
]
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.get_users),
    path("add/", views.add_user),
    path(
        'token/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path('notes', views.get_notes)
]

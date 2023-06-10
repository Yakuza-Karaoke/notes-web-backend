from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("user", views.UserList.as_view()),
    path("notes/", views.NoteList.as_view()),
    path("notes/<int:user_id>/", views.UserNotes.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.http import Http404

from db.models import Note
from api.serializers import NoteSerializer, UserSerializer
from api.permissions import IsAuthorOrReadOnly


class ApiRoot(APIView):
    def get(request, format=None):
        return Response(...)


class UserList(APIView):
    def get(self, request, format = None):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = self.request.user
        user.delete()

        return Response({"status": "deleted successfully"})

class NoteList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserNotes(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get(self, request, format=None):
        user = request.user
        notes = user.note_set.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    

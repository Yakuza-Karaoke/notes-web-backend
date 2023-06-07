from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from db.models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def get_users(request):
    User = get_user_model()
    users = User.objects.all()
    return Response()


@api_view(["POST"])
def add_user(request):
    # serializer = UserSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    # return Response(serializer.data)
    ...


def hash_password(pwd: str) -> str:
    ...


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)
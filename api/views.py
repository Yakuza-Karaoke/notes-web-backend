from rest_framework.response import Response
from rest_framework.decorators import api_view
from db.models import User
from .serializers import UserSerializer


@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def hash_password(pwd: str) -> str:
    ...
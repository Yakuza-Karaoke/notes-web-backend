from rest_framework import serializers
from django.contrib.auth.models import User
from db.models import Note


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Note.objects.all()
    )
    
    class Meta:
        model = User
        fields = ["id", "username", "notes"]


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Note
        fields = "__all__"

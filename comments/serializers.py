from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.StringRelatedField(source='user', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user_username', 'user_id', 'task', 'created_at']
        read_only_fields = ['id', 'created_at']

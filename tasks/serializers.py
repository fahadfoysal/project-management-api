from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_username = serializers.StringRelatedField(source='assigned_to', read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='assigned_to', write_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'assigned_to_username', 'assigned_to_id', 'project',
            'created_at', 'due_date',
        ]
        read_only_fields = ['id', 'created_at']

from rest_framework import serializers
from .models import Project, ProjectMember
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectMemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'user_id', 'role']
        read_only_fields = ['id', 'project']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner', write_only=True)
    members = ProjectMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_id', 'created_at', 'members']
        read_only_fields = ['id', 'created_at']

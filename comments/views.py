from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from tasks.models import Task 


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter comments by task id
        task_id = self.kwargs.get('task_id')
        if task_id:
            return Comment.objects.filter(task_id=task_id)
        return Comment.objects.all()

    def create(self, request, *args, **kwargs):
        # Ensure the task exists before creating a comment
        task_id = kwargs.get('task_id')
        task = get_object_or_404(Task, id=task_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(task=task, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

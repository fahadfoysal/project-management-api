from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/tasks/<int:task_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-comments'),
    path('api/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
    path('', include(router.urls)),
]

from django.urls import path, include
from .views import CommentViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(
    r'comment',
    CommentViewSet,
    basename='comment'
)

from rest_framework import viewsets
from .models import Comment
from .serializer import CommentSerializer
# Create your views here.

class Comment(viewsets.ModelViewSet):
    queryset = Comment.object.all()
    serializer_class = CommentSerializer

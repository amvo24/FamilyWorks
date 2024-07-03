from rest_framework import viewsets
from .models import Comment
# from .serializer import [enter serializer here]
# Create your views here.

class Comment(viewsets.ModelViewSet):
    queryset = Comment.object.all()
    # serializer_class = serialier

    

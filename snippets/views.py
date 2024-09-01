from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    """
    Use generics class-based views for get and post
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ 
        Associate the snippet with the user that created it, 
        by overwriting the perform_create method and passing 
        an additional `owner` field along the validated data
        from request
        """
        serializer.save(owner=self.request.user)
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Use generic class-based view to Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
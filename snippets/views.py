from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    """
    Use generics class-based views for get and post
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Use generic class-based view to Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

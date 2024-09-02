from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import SnippetViewSet, UserViewSet

# Create a router and register the ViewSets with it
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippet')
router.register(r'users', UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('', include(router.urls)),
]
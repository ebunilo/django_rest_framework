from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from .views import SnippetList, SnippetDetail, UserList, UserDetail, api_root, SnippetHighlight

urlpatterns = [
    path('', api_root),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('snipets/<int:pk>/highlight/', SnippetHighlight.as_view),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
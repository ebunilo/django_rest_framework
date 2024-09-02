# Django Rest Framework (DRF)

This repo implements an end-to-end Django Rest Framework for creating and managing snippets. It ties each snippet to the user that created it, hence it implements authentication and authorization for managing the snippets. The creator can edit and delete snippets while others can only view the snippets.

The final product uses ViewSets that is registered with the DefaultRouter for automatic routing.
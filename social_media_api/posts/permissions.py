from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow full access only to resource owners; read-only for others.
    """

    def has_object_permission(self, request, view, obj):
        # Safe methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Assume model has `author` field
        return getattr(obj, "author", None) == request.user


from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly, AllowAny


class IsCurrentUserOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        if request.user == obj:
            return True

        return False

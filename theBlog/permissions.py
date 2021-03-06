from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            return obj.author == request.user
        except:
            return obj.email == request.user.email

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.email == request.user.email

class IsUserOrReadOnlyProfile(permissions.BasePermission):
    def has_object_permission(self, request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user


class IsSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_superuser)

class ReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
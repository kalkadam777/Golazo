from rest_framework.permissions import BasePermission

class IsArticleWriter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Article Writer').exists()
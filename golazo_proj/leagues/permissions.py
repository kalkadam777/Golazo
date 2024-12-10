from rest_framework.permissions import BasePermission

class IsLeagueAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='League Admin').exists()


class IsTeamManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Team Manager').exists()
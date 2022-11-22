from rest_framework import permissions
import ipdb

class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == "GET":
            return True

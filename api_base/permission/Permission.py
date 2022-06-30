from rest_framework.permissions import BasePermission


class MyBasePermission(BasePermission):
    match_any_roles = []

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if not self.match_any_roles:
            return True

        for role in self.match_any_roles:
            if request.user.role_id.hex == role.value.get('id'):
                return True
        return False

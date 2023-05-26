from rest_framework import permissions


# if user is admin then he can do anything, other user will be read only
class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)
        # return request.method == "GET" or admin_permission
        if request.method in permissions.SAFE_METHODS:
            # check permission for read only request
            return True
        else:
            # check permission for write request
            return bool(request.user and request.user.is_staff)


# Object level permission
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # check permission for read only request
            return True
        else:
            # check permission for write request
            return obj.review_user == request.user

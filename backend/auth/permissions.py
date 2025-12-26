from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
	"""Allow only authenticated admins (role == ADMIN)."""

	def has_permission(self, request, view):
		return bool(
			request.user
			and request.user.is_authenticated
			and getattr(request.user, "role", None) == "ADMIN"
		)

	def has_object_permission(self, request, view, obj):
		return self.has_permission(request, view)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __str__(self):
		return "IsAdmin permission"

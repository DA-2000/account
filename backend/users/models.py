"""User domain models."""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class UserRole(models.TextChoices):
	USER = "USER", "User"
	ADMIN = "ADMIN", "Admin"


class User(AbstractUser):
	"""
	Username-first authentication user model.
	Used by both User and Admin frontends.
	"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	username = models.CharField(
		max_length=150,
		unique=True,
		help_text="Primary login identifier",
	)

	email = models.EmailField(
		unique=True,
		blank=False,
		null=False,
	)

	role = models.CharField(
		max_length=10,
		choices=UserRole.choices,
		default=UserRole.USER,
	)

	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)

	REQUIRED_FIELDS = ["email"]
	USERNAME_FIELD = "username"

	class Meta:
		db_table = "users"
		indexes = [
			models.Index(fields=["username"]),
			models.Index(fields=["email"]),
			models.Index(fields=["role"]),
		]

	def __str__(self) -> str:
		return f"{self.username} ({self.role})"

	@property
	def is_admin(self) -> bool:
		return self.role == UserRole.ADMIN

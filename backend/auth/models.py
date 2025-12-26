"""Social account linkage models."""

import uuid

from django.conf import settings
from django.db import models


class SocialProvider(models.TextChoices):
	GOOGLE = "google", "Google"
	GITHUB = "github", "GitHub"
	FACEBOOK = "facebook", "Facebook"


class SocialAccount(models.Model):
	"""Maps external OAuth providers to internal users."""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="social_accounts",
	)

	provider = models.CharField(
		max_length=20,
		choices=SocialProvider.choices,
	)

	provider_uid = models.CharField(
		max_length=255,
		help_text="User ID from the OAuth provider",
	)

	extra_data = models.JSONField(
		default=dict,
		blank=True,
	)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "social_accounts"
		unique_together = ("provider", "provider_uid")
		indexes = [
			models.Index(fields=["provider"]),
			models.Index(fields=["provider_uid"]),
		]

	def __str__(self) -> str:
		return f"{self.provider}:{self.provider_uid}"

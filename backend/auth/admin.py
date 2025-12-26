from django.contrib import admin

from .models import SocialAccount


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
	list_display = ("provider", "provider_uid", "user", "created_at")
	list_filter = ("provider",)
	search_fields = ("provider_uid", "user__username", "user__email")

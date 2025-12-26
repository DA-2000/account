"""Custom adapters for django-allauth integration."""

from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    """Hook for customizing account and signup flows."""

    pass

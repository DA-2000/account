"""User serializers for dj-rest-auth integration."""

from dj_rest_auth.serializers import UserDetailsSerializer

from users.models import User


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
            "is_active",
        )

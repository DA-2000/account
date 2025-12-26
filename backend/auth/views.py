from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from dj_rest_auth.views import LoginView
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
	post=extend_schema(
		tags=["Auth"],
		summary="Login",
		description="Authenticate user and issue JWT cookies",
	)
)
class RateLimitedLoginView(LoginView):
	"""Login endpoint with IP-based rate limiting."""

	@method_decorator(ratelimit(key="ip", rate="5/m", block=True))
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

"""All URLs of the UWUM social provider."""

from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import UWUMProvider


# Use the default OAuth2 provider URL patterns
urlpatterns = default_urlpatterns(UWUMProvider)

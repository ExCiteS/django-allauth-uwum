"""All views of the UWUM provider."""

from requests import get

from django.core.urlresolvers import reverse

from allauth.utils import build_absolute_uri
from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2View,
    OAuth2LoginView,
    OAuth2CallbackView,
)

from .client import UWUMClient
from .provider import UWUMProvider


class UWUMAdapter(OAuth2Adapter):
    """The UWUM OAuth2 adapter."""

    provider_id = UWUMProvider.id

    authorize_url = UWUMProvider.settings.get('AUTHORIZE_URL')
    access_token_url = UWUMProvider.settings.get('ACCESS_TOKEN_URL')
    profile_url = UWUMProvider.settings.get('PROFILE_URL')
    notify_email_url = UWUMProvider.settings.get('NOTIFY_EMAIL_URL')

    def make_request_headers(self, access_token):
        """Make the request headers by adding the bearer access token."""
        return {'Authorization': 'Bearer %s' % access_token}

    def get_notify_email(self, access_token):
        """Get the user (UWUM member) email address used for notifications."""
        headers = self.make_request_headers(access_token)
        response = get(self.notify_email_url, headers=headers).json()
        return response.get('result', {}).get('notify_email')

    def complete_login(self, request, app, access_token, **kwargs):
        """Complete the social login process."""
        headers = self.make_request_headers(access_token)
        params = {'include_member': True}
        response = get(self.profile_url, headers=headers, params=params).json()

        if app_settings.QUERY_EMAIL and response['member']:
            # Email address used for notifications will be a default user email
            response['member']['email'] = self.get_notify_email(access_token)

        return self.get_provider().sociallogin_from_response(request, response)


class UWUMView(OAuth2View):
    """The default UWUM OAuth2 view."""

    def get_client(self, request, app):
        """Get the UWUM client."""
        callback_url = reverse('%s_callback' % self.adapter.provider_id)
        callback_url = build_absolute_uri(request, callback_url)
        provider = self.adapter.get_provider()
        scope = provider.get_scope(request)

        return UWUMClient(
            request=self.request,
            consumer_key=app.client_id,
            consumer_secret=None,  # UWUM uses certificates instead
            access_token_method=self.adapter.access_token_method,
            access_token_url=self.adapter.access_token_url,
            callback_url=callback_url,
            scope=scope,
        )


class UWUMLoginView(UWUMView, OAuth2LoginView):
    """The UWUM OAuth2 login view."""

    pass


class UWUMCallbackView(UWUMView, OAuth2CallbackView):
    """The UWUM OAuth2 callback view."""

    pass


oauth2_login = UWUMLoginView.adapter_view(UWUMAdapter)
oauth2_callback = UWUMCallbackView.adapter_view(UWUMAdapter)

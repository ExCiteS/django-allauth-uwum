"""The UWUM (Unified WeGovNow User Management) provider."""

from distutils.version import StrictVersion

from allauth import __version__
from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class UWUMAccount(ProviderAccount):
    """The UWUM provider account."""

    pass


class UWUMProvider(OAuth2Provider):
    """The UWUM OAuth2 provider."""

    id = 'uwum'
    name = 'UWUM'
    settings = app_settings.PROVIDERS.get(id, {})
    account_class = UWUMAccount

    def get_default_scope(self):
        """Get the default UWUM scope."""
        default_scope = ['authentication']

        if app_settings.QUERY_EMAIL:
            default_scope.append('notify_email')

        return default_scope

    def extract_uid(self, data):
        """Extract the unique user (UWUM member) identification number."""
        member = data.get('member', {})
        return str(member.get('id'))

    def extract_common_fields(self, data):
        """Extract the common fields for the user (UWUM member)."""
        member = data.get('member', {})
        return {'username': member.get('name'), 'email': member.get('email')}


# The way provider is registered changed since django-allauth version 0.31.0
if StrictVersion(__version__) >= StrictVersion('0.31.0'):
    provider_classes = [UWUMProvider]
else:
    from allauth.socialaccount.providers.registry import register
    register(UWUMProvider)

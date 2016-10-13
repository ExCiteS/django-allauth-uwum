"""The UWUM (Unified WeGovNow User Management) provider."""

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers import registry
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
        return ['authentication', 'notify_email']

    def extract_uid(self, data):
        """Extract the unique user (UWUM member) identification number."""
        result = data['result']
        return str(result['member_id'])


registry.register(UWUMProvider)

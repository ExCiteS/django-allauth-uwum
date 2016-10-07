"""The UWUM (Unified WeGovNow User Management) client."""

from os import path
from requests import request

from allauth.socialaccount.providers.oauth2.client import (
    OAuth2Client,
    OAuth2Error,
)

from .provider import UWUMProvider


class UWUMClient(OAuth2Client):
    """The UWUM OAuth2 client."""

    def get_access_token(self, code):
        """Get the access token."""
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.consumer_key,
            'redirect_uri': self.callback_url,
            'code': code,
        }

        cert = UWUMProvider.settings.get('CERT')

        if not path.exists(cert):
            raise OAuth2Error('UWUM certificate not found')

        response = request(
            self.access_token_method,
            self.access_token_url,
            headers=self.headers,
            cert=cert,
            data=data,
        )

        access_token = None

        if response.status_code == 200:
            access_token = response.json()

        if not access_token or 'access_token' not in access_token:
            error = 'Error retrieving access token: %s' % response.content
            raise OAuth2Error(error)

        return access_token

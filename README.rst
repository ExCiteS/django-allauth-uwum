django-allauth-uwum
===================

An additional django-allauth social provider for UWUM (Unified `WeGovNow <http://wegovnow.eu/>`_ User Management).

Install
-------

Install django-allauth-uwum:

.. code-block:: console

    pip install git+https://github.com/ExCiteS/django-allauth-uwum.git

Add django-allauth and its social account apps to the list of installed apps.

Add django-allauth-uwum to the installed apps too:

.. code-block:: python

    INSTALLED_APPS += (
        'allauth_uwum',
    )

Create X.509 certificate signing request (CSR) and a new key:

.. code-block:: console

    openssl req -nodes rsa:2048 -new -out uwum.csr -newkey -keyout uwum.key

Client identification number will be the common name (CN) declared in the CSR.

Submit CSR to the UWUM Certificate Authority to be signed (key should be kept in secret).

Combine the signed CRT file with a key:

.. code-block:: console

    cat uwum.crt uwum.key > uwum.pem

Place a combined file (certificate) outside of the web directory.

Configure provider: add a full path to the certificate, also all the UWUM URLs. For example:

.. code-block:: python

    from os import path

    SOCIALACCOUNT_PROVIDERS = {
        'uwum': {
            'CERT': path.join(path.dirname(path.abspath(__file__)), 'uwum.pem'),
            'AUTHORIZE_URL': 'https://...',
            'ACCESS_TOKEN_URL': 'https://...',
            'PROFILE_URL': 'https://...',
        },
    }

Inform UWUM Certificate Authority of your callback URL, e.g.: `http://localhost/accounts/uwum/login/callback/`

You're now ready to go!

Update
------

Update django-allauth-uwum:

.. code-block:: console

    pip install -U git+https://github.com/ExCiteS/django-allauth-uwum.git

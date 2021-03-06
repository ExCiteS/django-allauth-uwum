django-allauth-uwum
===================

.. image:: https://travis-ci.org/ExCiteS/django-allauth-uwum.svg?branch=master
    :alt: Travis CI Build Status
    :target: https://travis-ci.org/ExCiteS/django-allauth-uwum

An additional django-allauth provider for UWUM (Unified `WeGovNow <http://wegovnow.eu/>`_ User Management).

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

    openssl genrsa -out uwum.key 2048
    openssl req -key uwum.key -new -sha256 -out uwum.csr

Client identification number will be the common name (CN) declared in the CSR.

Submit CSR to the UWUM Certificate Authority to be signed (key should be kept in secret).

Combine the signed CRT file with a key:

.. code-block:: console

    cat uwum.crt uwum.key > uwum.pem

Place a combined file (certificate) outside of the web directory.

Configure provider: add a full path to the certificate, also API version used alongside UWUM URLs. For example:

.. code-block:: python

    from os import path

    SOCIALACCOUNT_PROVIDERS = {
        'uwum': {
            'CERT': path.join(path.dirname(path.abspath(__file__)), 'uwum.pem'),
            'SCOPE': ['authentication', 'notify_email', 'post', 'rate', 'vote'],
            'REGULAR_URL': 'https://uwum-regular.server.dev',
            'CERT_URL': 'https://uwum-cert.server.dev',
            'API_VERSION': 1,
        },
    }

Any additional scope data can be added in the configuration of the UWUM provider. However, the default must be kept:

- `authentication` - allows to authenticate the user, also provides UWUM member ID and screen name.
- `notify_email` - allows to retrieve the email address used for notifications.

Inform UWUM Certificate Authority of your callback URL, e.g.: `http://localhost/accounts/uwum/login/callback/`

You're now ready to go!

Update
------

Update django-allauth-uwum:

.. code-block:: console

    pip install -U git+https://github.com/ExCiteS/django-allauth-uwum.git

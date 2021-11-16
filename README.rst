fluentcms-teaser
================

.. image:: https://github.com/django-fluent/fluentcms-teaser/actions/workflows/tests.yaml/badge.svg?branch=master
    :target: https://github.com/django-fluent/fluentcms-teaser/actions/workflows/tests.yaml
.. image:: https://img.shields.io/pypi/v/fluentcms-teaser.svg
    :target: https://pypi.python.org/pypi/fluentcms-teaser/
.. image:: https://img.shields.io/pypi/l/fluentcms-teaser.svg
    :target: https://pypi.python.org/pypi/fluentcms-teaser/
.. image:: https://img.shields.io/codecov/c/github/django-fluent/fluentcms-teaser/master.svg
    :target: https://codecov.io/github/django-fluent/fluentcms-teaser?branch=master

A teaser plugin for django-fluent-contents_

Originally authored by `Basil Shubin <https://github.com/bashu>`_.


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install fluentcms-teaser


Backend Configuration
---------------------

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_teaser',
    )

    # The upload folder for teasers
    # Default: '.'
    FLUENTCMS_TEASER_UPLOAD_TO = 'teasers/'

The database tables can be created afterwards:

.. code-block:: shell

    python ./manage.py migrate

Now, the ``TeaserPlugin`` can be added to your ``PlaceholderField`` and
``PlaceholderEditorAdmin`` admin screens.

Frontend Configuration
----------------------

If needed, the HTML code can be overwritten by redefining ``fluentcms_teaser/teaser.html``.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/django-fluent/django-fluent-contents

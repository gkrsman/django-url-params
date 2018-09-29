Django URL params
=================

Django-url-params is a reusable Django application allowing users to keep
URL parameters during redirection.


Requirements
------------

* **Django**: 1.10+


Installation
------------

Install using pip:

.. code-block:: sh

    pip install django-url-params

Then add ``'urlparams'`` to your ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'urlparams',
    ]


Usage
-----

Django-url-params can be used for generating interfaces similar to the Django
admin's ``list_filter`` interface.  It has an API very similar to Django's
``ModelForms``.  For example, if you had a Product model you could have a
filterset for it with the code:

.. code-block:: python

    from urlparams.redirect import param_redirect

    def my_view(request):
        # do something ...
        return param_redirect(request, 'view_name')


With django-url-params it's also possible to add parameter to your URL easily.

.. code-block:: python

    def my_view(request):
        request.cparam = {'my_parameter': 'my_value'}
        return param_redirect(request, 'view_name')

Parameter will be in your next url: ``.../my-url/?my_parameter=my_value``.
Note: function will keep existing parameters and append yours.

Usage with different URL conf
-----------------------------

Django-url-params provides a custom ``URL_PARAMS_CONF`` settings value for use with
different URL conf.

To use this add ``URL_PARAMS_CONF`` in your settings file.

.. code-block:: sh

    URL_PARAMS_CONF = 'my_custom.url_conf'


Django URL params
=================

Django-url-params is a reusable Django module allowing users to keep
URL parameters during redirection. It can be used for UTM parameters https://en.wikipedia.org/wiki/UTM_parameters or any other URL parameter. Especially when you need to use django redirect.


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

Usage is very simple:

.. code-block:: python

    from urlparams.redirect import param_redirect

    def my_view(request):
        # do something ...
        return param_redirect(request, 'view_name')


If your reverse url require arguments, just add it on the usual way:


.. code-block:: python

    def my_view(request):
        # do something ...
    return param_redirect(request, 'view_name', arg1, arg2)


With django-url-params it's also possible to add your parameter to the URL easily.

.. code-block:: python

    def my_view(request):
        request.cparam = {'my_parameter': 'my_value'}
        return param_redirect(request, 'view_name')

Parameter will be in your next url: ``.../my-url/?my_parameter=my_value``.

*Note:* function will keep existing parameters and append yours.

Usage with different URL conf
-----------------------------

Django-url-params provides a custom ``URL_PARAMS_CONF`` settings value for use with
different URL conf.

To use this add ``URL_PARAMS_CONF`` in your settings file.

.. code-block:: sh

    URL_PARAMS_CONF = 'my_custom.url_conf'


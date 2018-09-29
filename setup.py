import setuptools


LONG_DESCRIPTION = """Django URL params

This library contains code to expose some monitoring metrics relevant
to Django internals so they can be monitored by Prometheus.io.
See https://github.com/korfuri/django-prometheus for usage
instructions.
"""


setuptools.setup(
    name="django-url-params",
    version="1.0.1",
    author="Goran Krsman",
    author_email="goran@klikoglasi.com",
    description="Keep URL parameters in Django redirect.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/gkrsman/django-url-params",
    packages=setuptools.find_packages(),
    keywords=['django', 'url', 'redirect', 'django-url-params'],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

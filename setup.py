import setuptools


LONG_DESCRIPTION = """Django URL params

This library contains code to keep parameters in django URL 
during Django redirections.
"""


setuptools.setup(
    name="django-urlparams",
    version="1.0.1",
    author="Goran Krsman",
    author_email="goran@klikoglasi.com",
    description="Keep URL parameters in Django redirect.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/gkrsman/django-urlparams",
    packages=setuptools.find_packages(),
    keywords=['django', 'url', 'redirect', 'django-urlparams'],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

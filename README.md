# django-forums

[![Build Status](https://travis-ci.org/byteweaver/django-forums.svg?branch=master)](https://travis-ci.org/byteweaver/django-forums)

Small standalone django forums application.

## Key features

* Reusable forums app
* Templates use Bootstrap (twitter) styles
* ...

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-forums

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-forums#egg=django-forums

Add `forums` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'forums',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^forums/', include('forums.urls', namespace='forums')),
        ...
    )

## Versions

With the latest update, starting from version 0.1.x, django-forums supports django 1.5 and beyond. The default templates are now based on bootstrap-3.
If you use an older version of django or bootstrap, please have a look at version 0.9.0, but remember it is no longer maintained. The template syntax changed between django 1.4 and 1.5 (namespace of url tags are required to be quoted) so using a django version prior to 1.5 leads to template syntax errors.


## Tests

To run the tests you need the test runner `tox`:

    $ pip install tox

Then just call him:

    $ tox

## Tips and tricks

To improve the bootstrap form integration check out tzangms/django-bootstrap-form and override the forms.html template or have a look at issue #8 how to path the source code.

To override the template file make sure you add the application containing the new template first.

django-forums
===============

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
        url(r'^your-url/$', include('forums.urls')),
        ...
    )

## Versions

With the latest update, starting from version 0.1.x, django-forums supports django 1.5 and the default template now supports bootstrap-3.
If you use an older version of django or bootstrap, please have a look at version 0.9.0, but it is no supported.

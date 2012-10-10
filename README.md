django-skeleton
===============

skeleton for new django applications.

All following sections are just dummies and may not work as excepted.

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-skeleton
  
If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-skeleton#egg=django-skeleton

Add `skeleton` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'skeleton',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('skeleton.urls')),
        ...
    )


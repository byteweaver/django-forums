import os
from setuptools import setup, find_packages

import forums


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-forums',
    version=forums.__version__,
    description='Small standalone django forums application',
    long_description=read('README.md'),
    license='MIT License',
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-forums',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'django',
    ],
    tests_require=[
        'factory-boy',
    ],
    test_suite='runtests.runtests',
)

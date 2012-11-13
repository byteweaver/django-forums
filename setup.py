import os
from setuptools import setup, find_packages

import skeleton


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-skeleton',
    version=skeleton.__version__,
    description='skeleton for new django applications',
    long_description=read('README.md'),
    license='MIT License',
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-skeleton',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='skeleton.tests',
)

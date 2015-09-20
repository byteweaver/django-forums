SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'forums',
    'tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'tests.urls'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

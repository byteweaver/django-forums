from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)


class Forum(models.Model):
    category = models.ForeignKey(Category, related_name='forums')
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)

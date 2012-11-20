from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)


class Forum(models.Model):
    category = models.ForeignKey(Category, related_name='forums')
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)


class Topic(models.Model):
    forum = models.ForeignKey(Forum, related_name='topics')
    name = models.CharField(_("Name"), max_length=255)
    last_post = models.ForeignKey('Post', verbose_name=_("Last post"), related_name='forum_last_post', blank=True, null=True)



class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name='posts')
    user = models.ForeignKey(User, related_name='forum_posts')
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"),auto_now=True)
    body = models.TextField(_("Body"))

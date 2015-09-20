import factory
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from forums.models import Category, Forum, Topic, Post


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = 'Username'
    email = 'email@example.com'
    password = '123456'


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Category'


class ForumFactory(DjangoModelFactory):
    class Meta:
        model = Forum

    category = factory.SubFactory(CategoryFactory)
    name = 'Forum'


class TopicFactory(DjangoModelFactory):
    class Meta:
        model = Topic

    forum = factory.SubFactory(ForumFactory)
    name = 'Topic'


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    topic = factory.SubFactory(TopicFactory)
    user = factory.SubFactory(UserFactory)
    body = 'Body text\nWith multiple lines!'

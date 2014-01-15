import factory
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from forums.models import Category, Forum, Topic, Post


class UserFactory(DjangoModelFactory):
    FACTORY_FOR = get_user_model()

    username = 'Username'
    email = 'email@example.com'
    password = '123456'


class CategoryFactory(DjangoModelFactory):
    FACTORY_FOR = Category

    name = 'Category'


class ForumFactory(DjangoModelFactory):
    FACTORY_FOR = Forum

    category = factory.SubFactory(CategoryFactory)
    name = 'Forum'


class TopicFactory(DjangoModelFactory):
    FACTORY_FOR = Topic

    forum = factory.SubFactory(ForumFactory)
    name = 'Topic'


class PostFactory(DjangoModelFactory):
    FACTORY_FOR = Post

    topic = factory.SubFactory(TopicFactory)
    user = factory.SubFactory(UserFactory)
    body = 'Body text\nWith multiple lines!'

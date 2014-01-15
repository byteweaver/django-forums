import factory
from factory.django import DjangoModelFactory

from forums.models import Category, Forum


class CategoryFactory(DjangoModelFactory):
    FACTORY_FOR = Category

    name = 'Category'


class ForumFactory(DjangoModelFactory):
    FACTORY_FOR = Forum

    category = factory.SubFactory(CategoryFactory)
    name = 'Forum'

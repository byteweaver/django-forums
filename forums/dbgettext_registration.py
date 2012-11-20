from dbgettext.registry import registry, Options
from dbgettext.lexicons import html

from models import Category, Forum


class CategoryOptions(Options):
    attributes = ('name',)

class ForumOptions(Options):
    attributes = ('name')
    parsed_attributes = {'description': html.lexicon}

registry.register(Category, CategoryOptions)
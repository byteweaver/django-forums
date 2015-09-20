from django import template

from forums.models import Topic


register = template.Library()


class PopularTopicsListNode(template.Node):
    def render(self, context):
        context['popular_topics_list'] = Topic.objects.all()[:5]
        return u''


@register.tag
def get_popular_topics(parser, token):
    return PopularTopicsListNode()

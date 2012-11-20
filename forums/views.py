from django.views.generic import ListView, DetailView

from models import Category, Topic, Forum


class CategoryListView(ListView):
    model = Category

class ForumDetailView(DetailView):
    model = Forum

class TopicDetailView(DetailView):
    model = Topic

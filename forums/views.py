from django.views.generic import ListView, DetailView

from models import Category, Forum


class CategoryListView(ListView):
    model = Category

class ForumDetailView(DetailView):
    model = Forum

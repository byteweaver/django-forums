from django.conf.urls import patterns, url

from views import CategoryListView, ForumDetailView


urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name='overview'),
    url(r'^(?P<pk>\d+)/$', ForumDetailView.as_view(), name='forum'),
)

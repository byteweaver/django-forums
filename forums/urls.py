from django.conf.urls import patterns, url

from views import CategoryListView


urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name='overview'),
)

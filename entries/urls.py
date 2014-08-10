from django.conf.urls import patterns, url, include

from views import DetailView, CreateEntryView

urlpatterns = patterns('',
    url(r'^$',
        CreateEntryView.as_view(),
        name='index'),

    url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/$',
        DetailView.as_view(),
        name="detail"),

)

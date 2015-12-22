from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.{{ model_name }}List.as_view(), name='list'),
    url(r'^new/$', views.{{ model_name }}Create.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.{{ model_name }}Detail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.{{ model_name }}Update.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.{{ model_name }}Delete.as_view(), name='delete'),
]

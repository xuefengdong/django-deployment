from django.conf.urls import url
from basic_app import views

#template tagging
app_name = 'basic_app_tag'
urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]

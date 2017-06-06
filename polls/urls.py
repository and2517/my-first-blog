from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/index$', views.black, name='black'),
    url(r'^/index/black$', views.english, name='english'),
    url(r'^/index/inglish$', views.englishbl, name='russian'),
    url(r'^/name$', views.name, name='name'),

]
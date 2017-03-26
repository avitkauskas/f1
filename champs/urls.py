from django.conf.urls import url

from . import views

app_name = 'champs'
urlpatterns = [
    url(r'^$', views.years, name='years'),
    url(r'^champ/(?P<champ_year>[0-9]{4})/$', views.champ, name='champ'),
]

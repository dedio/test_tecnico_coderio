from django.conf.urls import url 
from swapi import views 
 
urlpatterns = [ 
    url(r'^character/(?P<idcharacter>[0-9a-zA-Z_]+)/$', views.get_character),
    url(r'^character/(?P<idcharacter>[0-9a-zA-Z_]+)/rating/(?P<rating>[0-9a-zA-Z_]+)/$', views.post_character),
]

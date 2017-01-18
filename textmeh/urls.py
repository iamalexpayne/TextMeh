from django.conf.urls import url

from . import views

# Official Routes

urlpatterns = [

    # Home Page
    url(r'^$', views.home_page, name='home_page'),

    # Registration Page
    url(r'^registration$', views.registration, name='registration'),

    # Chat Board Page
    url(r'^chat/(?P<username>\w+)/$', views.chat, name='chat'),

    # Chat Messages Page
    url(r'^chat/(?P<username>\w+)/messages$', views.messages, name='messages'),


]
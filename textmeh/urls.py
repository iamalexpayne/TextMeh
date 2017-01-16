from django.conf.urls import url

from . import views

# Oficial Routes

urlpatterns = [

    # Home Page
    url(r'^$', views.home_page, name='home_page'),

    url(r'^registration$', views.registration, name='registration'),



]
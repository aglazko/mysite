from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
]
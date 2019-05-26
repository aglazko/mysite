from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('place_list/',views.place_list, name='place_list')
]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'place_list/', views.placement_list, name='place_list'),
    url(r'rooms/', views.room_list, name='room_list'),
    url(r'houses/', views.house_list, name='house_list'),
    url(r'flats/', views.flat_list, name='flat_list'),
    url(r'rooms/<int:room_id>', views.room_get, name='room_get'),
    url(r'houses/<int:house_id>', views.house_get, name='house_get'),
    url(r'flats/<int:flat_id>', views.flat_get, name='flat_get'),
]

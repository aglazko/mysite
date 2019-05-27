from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place_list/', views.placement_list, name='place_list'),
    path('rooms/<int:room_id>/', views.room_get, name='room_get'),
    path('houses/<int:house_id>/', views.house_get, name='house_get'),
    path('flats/<int:flat_id>/', views.flat_get, name='flat_get'),
    path('rooms/', views.room_list, name='room_list'),
    path('houses/', views.house_list, name='house_list'),
    path('flats/', views.flat_list, name='flat_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('rooms/<int:room_id>/', views.room_get, name='room_get'),
    path('houses/<int:house_id>/', views.house_get, name='house_get'),
    path('flats/<int:flat_id>/', views.flat_get, name='flat_get'),
    path('placements/', views.placement_list, name='place_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('houses/', views.house_list, name='house_list'),
    path('flats/', views.flat_list, name='flat_list'),
    path('create/flat/', views.flat_create, name='flat_create'),
    path('create/room/', views.room_create, name='room_create'),
    path('create/house/', views.house_create, name='house_create'),
]

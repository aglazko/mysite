from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
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
    path('<type_>/<int:id>/approve/', views.approve, name='approve'),
    path('rooms/<int:id>/update/', views.room_update, name='room_update'),
    path('flats/<int:id>/update/', views.flat_update, name='flat_update'),
    path('houses/<int:id>/update/', views.house_update, name='house_update'),
    path('contracts/', views.contract_list, name='contract_list'),
    path('realtor_contracts/', views.realtor_contract_list, name='realtor_contract_list'),
    path('<type_>/<int:id>/contract', views.contract_create, name='contract_create'),
    path('contracts/<int:id>/approve', views.contract_approve, name='contract_approve')
]

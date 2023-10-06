from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('community/<int:pk>', community_detail, name='community-detail'),
    path('community-interface/<int:pk>', community_interface, name='community-interface'),
    path('add-community', add_community, name='add-community'),
    path('join-community/<int:pk>', join_community, name='join-community')
]
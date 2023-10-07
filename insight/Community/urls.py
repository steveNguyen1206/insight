from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('community/<int:pk>', community_detail, name='community-detail'),
    path('community-interface/home/<int:pk>', community_interface, name='community-interface'),
    path('community-interface/mentor/<int:pk>', community_mentor, name='community-mentor'),
    path('community-interface/setting/<int:pk>', community_setting, name='community-setting'),
    path('add-community', add_community, name='add-community'),

]
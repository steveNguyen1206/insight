from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('community/<int:pk>', CommunityDetail.as_view(), name='community-detail'),
    path('add-community', add_community, name='add-community')
]
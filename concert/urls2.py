from django.contrib import admin
from django.urls import path
from  .views2 import *

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('home_index/', admin_home, name='home_index'),
    path('allgame/', all_game, name='allgame'),
    path('Change_Password/', Change_Password, name='Change_Password'),
    path('Change_Password2/', Change_Password2, name='Change_Password2'),
    path('game_detail/<int:pid>/', game_detail, name='game_detail'),
]
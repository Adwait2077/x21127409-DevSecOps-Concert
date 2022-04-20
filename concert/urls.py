from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path('',home, name='home'),
    path('login/', sign_in, name='login'),
    path('register/', register, name='register'),
    path('edit_user/<int:pid>/',register,name="edit_user"),
    path('edit_game/<int:pid>/',Add_Game,name="edit_game"),
    path('register2/', register2, name='register2'),
    path('edit_user2/<int:pid>/',register2,name="edit_user2"),
    path('delete_user/<int:pid>/',delete_user,name="delete_user"),
    path('delete_book/<int:pid>/',delete_book,name="delete_book"),
    path('delete_game/<int:pid>/',delete_game,name="delete_game"),
    path('delete_category/<int:pid>/',delete_category,name="delete_category"),
    path('change_contact_status/<int:pid>/',change_contact_status,name="change_contact_status"),
    path('change_status/<int:pid>/',change_status,name="change_status"),
    path('change_game_category/<int:pid>/',add_game_category,name="change_game_category"),
    path('add_game_category/',add_game_category,name="add_game_category"),
    path('logout/', Logout, name='logout'),
    path('profile/', Single_Profile, name='profile'),
    path('add_game/',Add_Game, name='add_game'),
    path('book_ticket/<int:gid>/',book_ticket, name='book_ticket'),
    path('my_book/',my_book, name='my_book'),
    path('view_book/',view_booking, name='view_booking'),
    path('view_contact/',view_contact, name='view_contact'),
    path('view_contact_unread/',view_contact_unread, name='view_contact_unread'),
    path('new_user/',new_booking, name='new_booking'),
    path('all_user/',total_registered_user, name='total_registered_user'),
    path('view_game/',view_game, name='view_game'),   
    path('view_game_category/',view_game_category, name='view_game_category'),   
    path('search_between_dates/',search_between_dates, name='search_between_dates'),
    path('user_feedback/',user_feedback, name='user_feedback'),
    path('feedback_unread/',feedback_unread, name='feedback_unread'),
    path('change_FeedBack_status/<int:pid>/',change_FeedBack_status,name="change_FeedBack_status"),
    path('feedback_read/',feedback_read, name='feedback_read'),
       
]
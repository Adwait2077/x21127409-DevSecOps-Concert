from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Concert_Profile)

class GameAdmin(admin.ModelAdmin):
    list_display = ['user', 'game_name', 'total_seats', 'remaining_seats']
    search_fields = ('game_name',)
    list_filter = ('user', "created", )

admin.site.register(Concert, GameAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['game', 'user', 'booking_for', 'total_seats', 'total_price']
    search_fields = ('game', 'user')
    filter = ('user', "created")

admin.site.register(Booking,BookingAdmin)

admin.site.register(Contact)

admin.site.register(Feedback)

admin.site.register(Singer)
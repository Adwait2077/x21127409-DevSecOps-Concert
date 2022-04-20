from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.lookups import Transform

# Create your models here.
class Concert_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    contact_no = models.CharField(max_length=1000,null = True)
    address = models.CharField(max_length=1000,null = True)
    city = models.CharField(max_length=1000,null =True)
    images = models.FileField(null=True)
    created  = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True)
    
    def __str__(self):
        return(self.user.username)

STATUS_FEEDBACK = ((1, 'Read'), (2, "UnRead"))
class Feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank=True)
    description = models.CharField(max_length=5000,null=True)
    created  = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True)
    feedback_status = models.IntegerField(choices=STATUS_FEEDBACK , null = True, blank=True,default=2)
    
    def __str__(self):
        return self.user.username
    

class Singer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Concert(models.Model):
    category = models.ForeignKey(Singer, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank=True)
    game_name = models.CharField(max_length=100, null=True, blank=True)
    stadium_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total_seats = models.IntegerField(null=True, blank=True)
    local_seats = models.IntegerField(null=True, blank=True)
    vip_seats = models.IntegerField(null=True, blank=True)
    local_seats_price = models.IntegerField(null=True, blank=True)
    vip_seats_price = models.IntegerField(null=True, blank=True)
    remaining_seats = models.IntegerField(null=True, blank=True)
    last_booking = models.DateField(null=True, blank=True)
    game_date = models.DateField(null=True, blank=True)
    game_time = models.TimeField(null=True, blank=True)
    created  = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True, null=True)
    image = models.FileField(null = True)

    def __str__(self):
        return self.game_name


SEATS_CATEGORY = ((1, "VIP"), (2, "Local"))
STATUS = ((1, 'Pending'), (2, "Accepted"), (3, 'Canceled'))
class Booking(models.Model):
    status = models.IntegerField(choices=STATUS, null=True, blank=True, default=1)
    booking_id = models.CharField(max_length=100,null=True, blank=True)
    game = models.ForeignKey(Concert,on_delete=models.CASCADE,null = True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank=True)
    seat_choices = models.IntegerField(choices=SEATS_CATEGORY, null=True, blank=True)
    booking_for = models.DateField(null=True, blank=True)
    total_seats = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    created  = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.game.game_name
    
    
STATUS_CONTACT = ((1, 'Read'), (2, "UnRead"))
class Contact(models.Model):
    created = models.DateField(auto_now_add=True, null = True)
    contact_no = models.CharField(max_length=15, null = True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=1000,null=True)
    description = models.CharField(max_length=2000,null=True)
    contact_status = models.IntegerField(choices=STATUS_CONTACT , null = True, blank=True,default=2)
    
    def __str__(self) -> str:
        return self.first_name 
    

    

    
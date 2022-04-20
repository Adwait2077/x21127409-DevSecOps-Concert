from django import forms
from django.db.models import fields 
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model= Concert_Profile
        exclude= ('user','created','updated')
        
class GameForm(forms.ModelForm):
    class Meta:
        model = Concert
        exclude = ('user','created','updated', 'remaining_seats')

class GameCategoryForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['name', 'image']
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('user','created','updated')
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        exclude = ('created','contact_status')  
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user','created','updated')
        
from datetime import datetime
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
def about(request):
    feedback = Feedback.objects.all()
    return render(request,'about.html', {'feedback_data':feedback.order_by('-id')[0:10]})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent Successfully")
        else:
            print(form.errors)
    return render(request,'contact.html')

@login_required(login_url='/login/')
def admin_home(request):
    game = Concert.objects.all() 
    game_cat = Singer.objects.all() 
    book_all = Booking.objects.all() 
    book = Booking.objects.filter(status=1)
    
    stadium = Concert_Profile.objects.all() 
    return render(request, 'Admintemplates/admin_home.html',{'game_cat':game_cat.count(), 'game': game.count(), 'book_all':book_all.count(),'book':book.count(),'stadium':stadium.count()})

@login_required(login_url='/login/')
def all_game(request):
    game  = Concert.objects.filter(active=True)
    li = []
    tod = datetime.date.today()
    for i in game:
        if i.last_booking < tod or not i.remaining_seats:
            li.append(i.id)
    return render(request, 'all_game.html', {'game':game, 'li':li})

@login_required(login_url='/login/')
def Change_Password(request):
    if request.method=="POST":
        n = request.POST['password1']
        c = request.POST['password2']
        d = request.POST['password3']
        if c == d:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(d)
            u.save()
            messages.success(request, 'Password Changed Successfully')
    return render(request,'change_password.html')

@login_required(login_url='/login/')
def Change_Password2(request):
    if request.method=="POST":
        n = request.POST['password1']
        c = request.POST['password2']
        d = request.POST['password3']
        if c == d:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(d)
            u.save()
            messages.success(request, 'Password Changed Successfully')
    return render(request,'Admintemplates/change_password.html')


def game_detail(request,pid):
    data = Concert.objects.get(id=pid)
    li = []
    tod = datetime.date.today()
    if data.last_booking < tod or not data.remaining_seats:
        li.append(data.id)
    return render(request, 'game_detail.html', {'data':data, 'li':li})


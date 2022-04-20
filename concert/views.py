# from django.db.models.expressions import Random
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import datetime 
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def home(request):
    game = Concert.objects.all()
    feedback = Feedback.objects.all()
    game_cat = Singer.objects.all() 
    book_all = Booking.objects.all()
    newbooking = Booking.objects.filter(status=1).count()
    stadium = Concert_Profile.objects.all() 
    d = {'game_cat':game_cat.count(), 'game': game.count(),'newbooking':newbooking, 'book':book_all.count(),'total_user':stadium.count(), 'game_data':game.order_by('-id')[0:4],'feedback_data':feedback.order_by('-id')[0:10]}
    return render(request,'carousel.html', d)

def register(request,pid=None):
    profile = None
    user = None
    if pid:
        user = User.objects.get(id=pid)
        profile = Concert_Profile.objects.get(user=user)
    if request.method=='POST':
        form = RegisterForm(request.POST,request.FILES,instance=profile) #matching stadium profile attributes 
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        if form.is_valid():
            new_profile = form.save()
            if not profile:
                password = request.POST['password']
                user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
                new_profile.user = user
                messages.success(request, "Registration successfully")
                new_profile.save() 
                return redirect('login')
            else:
                user.first_name = fname
                user.last_name = lname
                user.email = email
                user.save()
                profile.user=user 
                profile.save()
                messages.success(request, "Updated successfully")
                return redirect('profile') 
        else:
            print(form.errors)
    d ={'profile':profile}
    return render(request,'register.html',d)

def register2(request,pid=None):
    profile = None
    user = None
    if pid:
        user = User.objects.get(id=pid)
        profile = Concert_Profile.objects.get(user=user)
    if request.method=='POST':
        form = RegisterForm(request.POST,request.FILES,instance=profile) #matching stadium profile attributes 
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        if form.is_valid():
            new_profile = form.save()
            if not profile:
                password = request.POST['password']
                user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
                new_profile.user = user
                new_profile.save()
                messages.success(request, "Registration successfully")
                return redirect('login')
            else:
                user.first_name = fname
                user.last_name = lname
                user.email = email
                user.save()
                profile.user=user 
                messages.success(request, "Updated successfully")
                profile.save()
                return redirect('total_registered_user')  
        else:
            print(form.errors)
    d ={'profile':profile}
    return render(request,'Admintemplates/register2.html',d)
        

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password) #check the exixting user
        if user.is_staff:
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('home_index')
        elif user:
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "Username and Password are invalid.")
    return render(request,'login.html')
        
@login_required(login_url='/login/')
def Single_Profile(request):  #get single data 
    single_data = Concert_Profile.objects.get(user=request.user)
    dict = {
        'data':single_data
    }
    return render(request,'profile.html',dict)

@login_required(login_url='/login/')
def All_Profile(request):  # getmultiple data
    single_data = Concert_Profile.objects.all()
    dict = {
        'data':single_data
    }
    return render(request,'contact.html',dict)

@login_required(login_url='/login/')
def delete_user(request,pid):
    profile = Concert_Profile.objects.get(id = pid)
    profile.delete()
    messages.success(request, "Deleted successfully")
    return redirect('total_registered_user')

@login_required(login_url='/login/')
def delete_book(request,pid):
    profile = Booking.objects.get(id = pid)
    profile.delete()
    messages.success(request, "Deleted successfully")
    return redirect('view_booking')

@login_required(login_url='/login/')
def Logout(request):
    messages.success(request, "Logout Successfully")
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def Add_Game(request,pid=None):
    game_cat = Singer.objects.all()
    game = None
    if pid:
        game = Concert.objects.get(id=pid)
    if request.method == 'POST':
        form = GameForm(request.POST,request.FILES,instance=game)
        if form.is_valid():
            new_game = form.save()
            #new_game.remaining_seats = 80
            new_game.user = request.user
            if not pid:
                new_game.remaining_seats = new_game.total_seats
                messages.success(request, "Added successfully")
            else:
                messages.success(request, "Updated successfully")
            new_game.save()
            #messages.success(request, "Added successfully")
            return redirect('view_game')
    d = {'game':game, 'category':game_cat}
    return render(request,'add_game.html',d)
 
@login_required(login_url='/login/')          
def book_ticket(request,gid, pid=None):
    game = Concert.objects.get(id=gid)
    book_ticket = None
    if pid:
        book_ticket = Booking.objects.get(id=pid)
    if request.method == 'POST':
        form = BookingForm(request.POST,request.FILES,instance=book_ticket)
        if form.is_valid():
            new_booking = form.save()     
            new_booking.user = request.user
            new_booking.status = 1
            random_number = 0
            while(1):
                random_number = random.randint(1000000000, 9999999999)
                try:
                    Booking.objects.get(booking_id = random_number)
                except:
                    new_booking.booking_id = random_number
                    new_booking.save()
                    break
            new_booking.game.remaining_seats -= int(request.POST.get('total_seats'))
            new_booking.save()
            new_booking.game.save()
            messages.success(request, "Booked successfully")
            return redirect('my_book')
        else:
            print(form.errors)
    d = {'book_ticket':book_ticket, 'seat':SEATS_CATEGORY, 'game':game}
    return render(request, 'book.html',d)

@login_required(login_url='/login/')              
def my_book(request):
    book =  Booking.objects.filter(user=request.user)
    return render(request, 'my_booking.html',{'book':book})

@login_required(login_url='/login/')
def view_booking(request):
    view_book = Booking.objects.all()
    if request.method == "POST":
        search = request.POST['search']
        view_book = view_book.filter(booking_id=search)
    return render(request, 'Admintemplates/view_booking.html',{'view_book':view_book})
   
@login_required(login_url='/login/')    
def new_booking(request):
    new_book = Booking.objects.filter(status=1)
    return render(request, 'Admintemplates/new_booking.html',{'new_user':new_book})

@login_required(login_url='/login/')
def total_registered_user(request):
    all_user = Concert_Profile.objects.all()
    return render(request, 'Admintemplates/total_registered_user.html',{'all_profile_registered':all_user})

@login_required(login_url='/login/')
def view_game(request):
    v_game = Concert.objects.all()
    return render(request, 'Admintemplates/view_game.html',{'game_info':v_game})

@login_required(login_url='/login/')
def change_status(request, pid):
    book = Booking.objects.get(id = pid)
    if request.user.is_staff:
        if book.status == 1:
            book.status = 2
            book.save()
        elif book.status == 2:
            book.status = 1
            book.save()
        messages.success(request, "Status changed successfully")
        return redirect('view_booking')
    else:
        book.status = 3
        book.save()
        messages.success(request, "Status changed successfully")
        return redirect('my_book') 

@login_required(login_url='/login/')
def delete_game(request,pid):
    game = Concert.objects.get(id=pid)
    game.delete()
    messages.success(request, "Deleted successfully")
    return redirect("view_game")

@login_required(login_url='/login/')
def delete_category(request,pid):
    game = Singer.objects.get(id=pid)
    game.delete()
    messages.success(request, "Deleted successfully")
    return redirect("view_game_category")

@login_required(login_url='/login/')
def add_game_category(request, pid=None):
    game_cat = None
    if pid:
        game_cat = Singer.objects.get(id=pid)
    if request.method == "POST":
        form = GameCategoryForm(request.POST, request.FILES, instance=game_cat)
        if form.is_valid():
            form.save()
            if pid:
                messages.success(request, "Updated successfully")
            else:
                messages.success(request, "Added successfully")
            return redirect('view_game_category')
    d = {'game': game_cat}
    return render(request, 'Admintemplates/add_game_category.html', d)

@login_required(login_url='/login/')
def view_game_category(request):
    v_game = Singer.objects.all()
    return render(request, 'Admintemplates/view_game_category.html',{'game_info':v_game})

@login_required(login_url='/login/')
def search_between_dates(request):
    book = None
    if request.method == "POST":
        d1 = request.POST['d1']
        d2 = request.POST['d2']
        book = Booking.objects.filter(booking_for__gte = datetime.datetime.strptime(d1,'%Y-%m-%d'), booking_for__lte=datetime.datetime.strptime(d2,'%Y-%m-%d'))
        
    return render(request, 'Admintemplates/search_between_dates.html', {'book':book,'d1':d1,'d2':d2})

@login_required(login_url='/login/')
def view_contact(request):  #view contact read
    v_game = Contact.objects.filter(contact_status = 1)
    return render(request, 'view_contact.html',{'contact_info':v_game})

@login_required(login_url='/login/')
def view_contact_unread(request):
    v_game = Contact.objects.filter(contact_status = 2)
    return render(request, 'view_contact_unread.html',{'contact_info':v_game})

@login_required(login_url='/login/')
def change_contact_status(request, pid):
    book = Contact.objects.get(id = pid)
    book.contact_status = 1
    book.save()
    messages.success(request, "Status changed successfully")
    return redirect('view_contact') 

@login_required(login_url='/login/')
def user_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            new_feedback = form.save()
            new_feedback.user = request.user 
            new_feedback.save()
            messages.success(request,"message submitted successfully")
    return render(request,'user_feedback.html')

@login_required(login_url='/login/')    
def feedback_unread(request):
    f_unread = Feedback.objects.filter(feedback_status = 2)
    return render(request, 'Admintemplates/feedback_unread.html',{'feedback_info':f_unread})

@login_required(login_url='/login/')
def feedback_read(request):
    f_unread = Feedback.objects.filter(feedback_status = 1)
    return render(request, 'Admintemplates/feedback_read.html',{'feedback_info':f_unread})

@login_required(login_url='/login/')
def change_FeedBack_status(request, pid):
    fb = Feedback.objects.get(id = pid)
    fb.feedback_status = 1
    fb.save()
    messages.success(request, "Status changed successfully")
    return redirect('feedback_read') 
    
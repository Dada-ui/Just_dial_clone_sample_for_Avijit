from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from q.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def cover(request):
    return render(request,'cover.html')


def home(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Error : please login')
        return redirect('login')
    return render(request,'home.html')


def services(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        products = Product.objects.all()
        return render(request,'services.html',{'products' : products})


def about(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'about.html')


def contactview(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        messages.success(request,'Thanks for contacting us.. Have a nice day...!!!') 
    return render(request,'contact.html')


def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.GET.get('query'):
        return HttpResponseRedirect(request,'Categories Not Available')
    else:
        query = request.GET.get('query')
        products = Product.objects.filter(role__icontains = query)
        return render(request,'search.html',{'products' : products})
        

def loginview(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user1=authenticate(username=username,password=password)
            if user1 is not None:
                login(request,user1)
                return redirect('home')
        return render(request,'login.html')
    else:
        return redirect('home')


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return redirect('login')
    return render(request,'logout.html')


def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':

            # Checking Already Data Has Been Recorded or Not..!

            # Username
            '''if User.objects.filter(username = request.POST['username']):
                messages.warning(request,'Username already exists')
                return render(request,'register.html')

            # Phone Number
            elif User.objects.filter(phone = request.POST['phone']):
                messages.warning(request,'Phone number already exists')
                return render(request,'register.html')

            # Re - Phone Number
            elif User.objects.filter(rephone = request.POST['rephone']):
                messages.warning(request,'Phone number not same')
                return render(request,'register.html')

            # Email
            elif User.objects.filter(email = request.POST['email']):
                messages.warning(request,'Email address already exists')
                return render(request,'register.html')

            # Re - Email
            elif User.objects.filter(reemail = request.POST['reemail']):
                messages.warning(request,'Email address not same')
                return render(request,'register.html')'''

            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            reemail = request.POST['reemail']
            password = request.POST['password']
            repassword = request.POST['repassword']

            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.reemail = reemail
            user.repassword = repassword
            user.save()
            return redirect('login')
        
        return render(request,'register.html')
    else:
        return redirect('home')


def loginview(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user1=authenticate(username=username,password=password)
            if user1 is not None:
                login(request,user1)
                return redirect('home')
        return render(request,'login.html')
    else:
        return redirect('home')



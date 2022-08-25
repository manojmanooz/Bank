from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Details
# Create your views here.
def home(request):
    return render(request,'base.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,"Sign up completed")
                return redirect('login')

        else:
            messages.info(request,"Sign Up Failed")
    return render(request,'Register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,username)
            return redirect('welcome')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')

    return render(request,'login.html')


def welcome(request):
    return render(request,'welcome.html')


def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        date=request.POST['date']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        sm = request.POST.get("male")
        if sm == 'on':
            sm = True
        else:
            sm = False
        sf = request.POST.get("female")
        if sf == 'on':
            sf = True
        else:
            sf = False
        district=request.POST['slct1']
        branch=request.POST['slct2']
        sc = request.POST.get("credit")
        if sc == 'on':
            sc = True
        else:
            sc = False
        sd = request.POST.get("debit")
        if sd == 'on':
            sd = True
        else:
            sd = False
        sq = request.POST.get("cheque")
        if sq == 'on':
            sq = True
        else:
            sq = False
        user=Details(name=name,date=date,email=email,phone=phone,age=age,district=district,branch=branch,male=sm,female=sf,credit=sc,debit=sd,cheque=sq)
        user.save()
        messages.info(request,"Registered Successfully")
        return redirect('/')
    return render(request,'form.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def index(r):
    return render(r,'index.html')

def makeorder(r):
    if r.method=='POST':
        ctype = r.POST['cargo-type']
        cweight = float(r.POST['cargo-weight'])
        ctime = int(r.POST['cargo-time'])
        cplace = r.POST['cargo-place']
        pnumber = str(r.POST['pnumber'])
    else:
        return render(r,'makeorder.html')

def vieworders(r):
    return render(r,'vieworders.html')

def estimateprices(r):
    return render(r,'estimateprices.html')

def login(r):
    if r.method=='POST':
        uname = r.POST['uname']
        pword = r.POST['pword']
        user = auth.authenticate(username=uname,password=pword)
        if user:
            auth.login(r,user)
            res = redirect('/')
            res.set_cookie('user',uname)
            return res
        msg = "Invalid Username or Password."
        return render(r,'login.html',{'msg':msg})
    else:
        return render(r,'login.html')

def logout(r):
    auth.logout(r)
    res = redirect('/')
    res.delete_cookie('user')
    return res

def register(r):
    if r.method=='POST':
        uname = r.POST['uname']
        fname = r.POST['fname']
        lname = r.POST['lname']
        email = r.POST['ename']
        pword = r.POST['pword']
        rpword = r.POST['rpword']
        if pword == rpword:
            if User.objects.filter(username=uname):
                msg = "Username is already taken"
                return render(r,'register.html',{'msg':msg})
            elif User.objects.filter(email=email):
                msg = "E-mail is already registered"
                return render(r,'register.html',{'msg':msg})
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,password=pword,username=uname,email=email)
                user.save();
                auth.login(r,user)
                return redirect('/')
        else:
            msg = "Passwords do not match"
            return render(r,'register.html',{'msg':msg})
    else:
        return render(r,'register.html')
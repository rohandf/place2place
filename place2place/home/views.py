from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import order


# Create your views here.

def index(r):
    return render(r,'index.html')

def makeorder(r):
    if r.method=='POST':
        user_id = r.user.id
        ctype = r.POST['cargo-type']
        cweight = float(r.POST['cargo-weight'])
        ctime = int(r.POST['cargo-time'])
        cplace = r.POST['cargo-place']
        pnumber = str(r.POST['pnumber'])
        obj = order.objects.create(order_id=user_id,cargo_type=ctype,cargo_weight=cweight,delivery_time=ctime,cargo_destination=cplace,phone_number=pnumber)
        # order_id is incorrectly named, it is the ID of the user who placed the order.
        # refer to order_number for the actual order ID.
        obj.save()
        return redirect('/vieworders')

    else:
        return render(r,'makeorder.html')

def vieworders(r):
    orders_data = order.objects.filter(order_id=r.user.id)
    return render(r,'vieworders.html',{'orders_data':orders_data})

def estimateprices(r):
    if r.user.is_staff:
        orders_data = order.objects.all()
        print(orders_data)
        return render(r,'estimateprices.html',{'orders_data':orders_data})
    else:
        return redirect('/')

def editprice(r):
    if r.method=='POST' and r.user.is_staff:
        order_id=r.POST['order-id']
        newprice = float(r.POST['n-price'])
        order.objects.filter(order_number=order_id).update(price=newprice)
        #obj.save()
        return redirect('/estimateprices/')
    elif r.method=='GET' and r.user.is_staff:
        if r.META.get('HTTP_REFERER'): # allows accessing the page only from estimateprices page
            order_id = r.GET['order_id']
            order_data = order.objects.filter(order_number=order_id)[0]
            return render(r,'editprice.html',{'order':order_data})
        else:
            return redirect('/estimateprices/')
    else:
        return redirect('/')

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
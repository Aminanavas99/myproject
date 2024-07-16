from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from .models import Customer

# Create your views here.


def sign_out(request):
    logout(request)
    return redirect('home')


def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            print(request.POST)
            # create user accnt
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # create customer object
            customer = Customer.objects.create(user=user, name=user.username, address=address)
            success_msg='user registered succefully'
            messages.success(request,success_msg)
            # return redirect('home')
        except Exception as e:
            error_msg='duplictaes not allowed!@.....'
            messages.error(request,error_msg)

    if request.POST and 'login' in request.POST:
        context['register']=False
            
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_msg='user not found'
            messages.error(request,error_msg)
                 



    
    return render(request,'account.html',context)


# for a guest user no need to show the cart option
# for a logined person no need to show the accnt tab
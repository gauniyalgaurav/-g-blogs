from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('write')
        else:
            messages.info(request,'*credentials invalid*')
            return redirect('login')
    else:
        return render (request,'login.html')
def about(request):
    return render (request,'about.html')
def write(request):
    return render(request,'write.html')
def sign(request):
    if request.method=='POST':
        username=request.POST.get('username',False) 
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        gender=request.POST.get('gender',False)
        
        if User.objects.filter(email=email).exists():
            messages.info("email already exists")
            return redirect('sign')
        else:
            
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
    else:
        return render (request,'sign.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
def write(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid:
                form.save()
                form = PostForm()
       
        else:
            form = PostForm()
        return render(request,'write.html',{'form':form})
    else:
        return redirect('login')
def posts(request):
    posts=Post.objects.all()
    return render(request,'posts.html',{'posts':posts})
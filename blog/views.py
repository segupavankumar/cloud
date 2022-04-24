from django.shortcuts import redirect, render
from .models import blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm,AddBlog
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'login.html')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'register.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    blogs = blog.objects.all()
    name = User.username
    # print(blogs[0].img1)
    run = True
    if len(blogs) ==0:
        run = False
    # return render(request,'home.html',{'blogs':blogs,'run':run})
    return render(request,'home.html',{'blogs':blogs,'User':User,'run':run})
    # return render(request,'home.html')

def add_blog(request):
    if request.method == 'POST':
        form = AddBlog(request.POST,request.FILES)
        print('hi',form)
  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = AddBlog()
    return render(request, 'add.html', {'form' : form})

@login_required
def my_blog(request):
    blogs = blog.objects.filter(user = request.user)
    run = True
    if len(blogs) ==0:
        run = False
    return render(request,'home.html',{'blogs':blogs,'run':run})


def blog_view(request,id):
    blogs = blog.objects.get(id=id)
    run = True
    return render(request,'blog_view.html',{'blog':blogs,'run':run})
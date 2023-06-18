from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm
from . models import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    user = User()
    if user.is_authenticated:
        if request.method == "POST":
            fm = ImageForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
        fm = ImageForm()
        img = Image.objects.all()
        return render(request, 'myapp/home.html', {"fm": fm, 'img': img})
    else:
        return render(request, 'myapp/login.html',)


def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
    return render(request, 'myapp/signup.html',)


def userlogin(request):
    user = User()
    if not user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('name')
            password = request.POST.get('pass')
            usr = authenticate(request, username=username, password=password)
            if usr is not None:
                login(request, user)
                return render(request, 'myapp/home.html', {"fm": fm, 'img': img})
    return render(request, 'myapp/login.html',)


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def userdelete(request, id):
    uid = Image.objects.get(id=id)
    uid.delete()
    return HttpResponseRedirect('/')

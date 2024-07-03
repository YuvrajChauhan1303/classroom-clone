# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == "POST":

        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=email).exists():
            messages.add_message(request, messages.ERROR, 'Email is already taken')
            return render(request, "authentication/register.html")

        user = User.objects.create(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
    
        login(request, user)

        return redirect("/")
    else:
        return render(request, "authentication/register.html")
    


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(email = email, password=password, username=email)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect Login Credentials')
            return render(request, "authentication/login.html")
    else:
        return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return redirect("/api/auth/login")
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout )
from django.contrib.auth.models import User
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return render(request, "login/login.html")
        else:
            error = "다시 시도해주세요"
            return render(request, "login/login.html", { "error" : error})
    else:
        return render(request, "login/login.html")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if form.is_valid() and cpassword == password:
            new_user = User.objects.create_user(**form.cleaned_data)
            django_login(request, new_user)
            return render(request, "login/login.html")
        else:
            context = {"msg" : "회원가입 실패"}
            return render(request, "login/signup.html", context)
    else:
        form = UserForm()
        return render(request, "login/signup.html")

def logout(request):
    django_logout(request)
    return render(request, "login/login.html")

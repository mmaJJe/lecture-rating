from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout )
from django.contrib.auth.models import User
from main.models import Profile
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
            datas= Profile.objects.get(user=request.user)
            college =  datas.university
            request.session['college'] = college
            return redirect("search_home")
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
            userdata = Profile()
            userdata.user = request.user
            userdata.university = request.POST['university'] # 추가됨
            userdata.major = request.POST['major'] # 추가됨
            userdata.admission_year = request.POST['admission_year'] # 추가됨
            userdata.save() # 추가됨
            request.session['college'] = request.POST['university']
            return redirect("search_home")

        else:
            context = {"msg" : "회원가입 실패1" }
            return render(request, "login/signup.html", context)
    else:
        context = {"msg" : "회원가입 실패2"}
        form = UserForm()
        return render(request, "login/signup.html")

def logout(request):
    django_logout(request)
    return render(request, 'main/home.html')

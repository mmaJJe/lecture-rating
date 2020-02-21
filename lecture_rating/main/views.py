from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import University, LectureRatingBoard, Lecture
# Create your views here.

def home (request) :
    if request.session.get('college') :
        return redirect("search_lecture")

    return render(request, 'main/home.html')

def find_college(request) :
    re_college = request.POST.get('college')
    fi_college = University.objects.filter(name__icontains = re_college)

    context = {'colleges' : fi_college}

    return render(request, 'main/college.html', context)

def search_lecture (request) :
    type_name = request.POST.get("type")
    search_content = request.POST.get("search_content")
    univer = reqeust.session.get('college')
    college = University.objects.get(name=univer)
    if type_name == "Lecture Title" :
        lectures = Lecture.objects.filter(name__icontains=search_content, university=college)
        for lecture in lectures :
            results = LectureRatingBoard.objects.filter(lecture = lecture)
    elif type_name == "Professor" :
        professor = Porfessor.objects.filter(name__icontains=search_content, university=college)
        lectures = Lecture.objects.filter(professor=professor, university=college)
        for lecture in lectures :
            results = LectureRatingBoard.objects.filter(lecture = lecture)
    elif type_name == "Content" :
        results = LectureRatingBoard.objects.filter(content__icontains=search_content, university=college)
    elif type_name == "Lecture Code" :
        lectures = Lecture.objects.filter(lecture_id=search_content, university=college)
        for lecture in lectures :
            results = LectureRatingBoard.objects.filter(lecture=lecture)
    
    return render()

def choose_college(request) :
    college = request.POST.get('college')
    request.session['college'] = college
    
    return redirect("search_lecture")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from .models import University, LectureRatingBoard, Lecture, Professor
from django.db.models import Subquery, OuterRef
from django.core.paginator import Paginator
# Create your views here.

# 맨 처음 메인화면 띄우기
def home (request) :
    if request.GET.get('college_del') :
        del request.session['college']
    if request.session.get('college') :
        return redirect("search_home")

    return render(request, 'main/home.html')

# 입력한 대학교 찾기
def find_college(request) :
    re_college = request.POST.get('college')
    fi_college = University.objects.filter(name__icontains = re_college)
    # 입력한 문자열을 통해 filter로 해당 여러 대학 찾기
    context = {'colleges' : fi_college}
    return render(request, 'main/college.html', context)

# 내가 원하는 강의 찾기
# Subquery를 이용하여 내가 원하는 강의 찾기
def search_lecture (request) :

    list_lecture = []
    type_name = request.POST.get("type")
    search_content = request.POST.get("search_content")
    univer = request.session.get('college')
    college = University.objects.get(name=univer)

    # 강의 제목으로 검색했을 때 강의 맞는 강의 제목을 찾고 그에 해당하는 강의평가 게시물 검색
    if type_name == "Lecture Title" :
        results = LectureRatingBoard.objects.filter(
            lecture = Subquery(Lecture.objects.filter(name__icontains=search_content, university=college)))
        
        # lectures = Lecture.objects.filter(name__icontains=search_content, university=college)
        # for lecture in lectures :
        #     results = LectureRatingBoard.objects.filter(lecture = lecture)


    # 강의자, 교수님으로 찾을 때 해당 교수님의 data를 먼저 찾고, 교수님이 해당하는 강의를 검색 후에 강의평가 게시물 확인
    elif type_name == "Professor" :
        results = LectureRatingBoard.objects.filter(
            lecture = Subquery(Lectrue.objects.filter(
                professor= Subquery(Professor.objects.filter(name__icontains=search_content, university = college)))))

        # professor = Porfessor.objects.filter(name__icontains=search_content, university=college)
        # lectures = Lecture.objects.filter(professor=professor, university=college)
        # for lecture in lectures :
        #     results = LectureRatingBoard.objects.filter(lecture = lecture)

    # 강의 평가 내용으로 찾기
    elif type_name == "Content" :
        results = LectureRatingBoard.objects.filter(content__icontains=search_content, university=college)
    # 강의 코드 즉, 강의 자체 코드에 대해서 검색
    elif type_name == "Lecture Code" :
        results = LectureRatingBoard.objects.filter(lecture = Subquery(Lecture.objects.filter(lecture_id=search_content, university=college)))
        
        
        # lectures = Lecture.objects.filter(lecture_id=search_content, university=college)
        # for lecture in lectures :
        #     results = LectureRatingBoard.objects.filter(lecture=lecture)
    
    elif type_name == "User" :
        results = LectureRatingBoard.objects.filter(user = Subquery(User.objects.filter(userid=search_content, university=college)))
    
    # return render(request)

def search_home(request) :
    lec_list = LectureRatingBoard.objects.all()
    paginator = Paginator(lec_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context= {'lec_li':lec_list, 'posts':posts,}
    return render(request, "main/lecture_search.html", context)

def choose_college(request) :
    college = request.POST.get('college')
    request.session['college'] = college
    
    return redirect("search_home")

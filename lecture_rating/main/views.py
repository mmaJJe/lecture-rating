from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from .models import University, LectureRatingBoard, Lecture, Professor
from django.db.models import Subquery, OuterRef, Avg, Max
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
    type_name = request.POST.get("search_type")
    search_content = request.POST.get("search_content")
    univer = request.session.get('college')
    college = University.objects.get(name=univer)
    print(search_content)

    # 강의 제목으로 검색했을 때 강의 맞는 강의 제목을 찾고 그에 해당하는 강의평가 게시물 검색
    if type_name == "Lecture Title" :
        # results = LectureRatingBoard.objects.filter
        results = Lecture.objects.filter(name__icontains=search_content, university=college)
        
        # results = []
        # for lec in lecture :
        #     results.append(get_object_or_404(LectureRatingBoard, lecture=lec))


    # 강의자, 교수님으로 찾을 때 해당 교수님의 data를 먼저 찾고, 교수님이 해당하는 강의를 검색 후에 강의평가 게시물 확인
    elif type_name == "Professor" :
        results = Lecture.objects.filter(
            professor = Subquery(Professor.objects.filter(name__icontains=search_content, university = college).values('id')[:1]))


        # results = []
        # for lec in lecture :
        #     results.append(get_object_or_404(LectureRatingBoard, lecture=lec))

    # 강의 코드 즉, 강의 자체 코드에 대해서 검색
    elif type_name == "Lecture Code" :
        # results = LectureRatingBoard.objects.filter(lecture = Subquery(
        results = Lecture.objects.filter(lecture_id=search_content, university=college).values('id')[:1]
        
        
        # lectures = Lecture.objects.filter(lecture_id=search_content, university=college)
        # for lecture in lectures :
        #     results = LectureRatingBoard.objects.filter(lecture=lecture)
    
    stars= {}
    lec_list = results
    for lecture in lec_list :
        stars[lecture] = LectureRatingBoard.objects.filter(lecture=lecture).aggregate(Avg('stars')).get('stars__avg')

    paginator = Paginator(lec_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'lec_li' : lec_list, 'posts':posts, 'stars': stars}

    return render(request, "main/lecture_search.html", context)

def search_home(request) :
    stars = {}
    lec_list = Lecture.objects.all()
    for lecture in lec_list :
        stars[lecture] = LectureRatingBoard.objects.filter(lecture=lecture).aggregate(Avg('stars')).get('stars__avg')
    # lec_list = LectureRatingBoard.objects.all()
    paginator = Paginator(lec_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context= {'lec_li':lec_list, 'posts':posts, 'stars' : stars}
    print(posts)
    print(stars)
    return render(request, "main/lecture_search.html", context)

def lecture_detail(request, lecture_id) :
    lecture = get_object_or_404(Lecture, lecture_id=lecture_id)
    star = request.GET.get('star')
    lec_list = LectureRatingBoard.objects.filter(lecture=lecture)

    paginator = Paginator(lec_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'lec_li':lec_list, 'posts':posts, 'star' : star, 'lecture' : lecture}

    return render(request, 'main/lecture_detail.html', context)

def choose_college(request) :
    college = request.POST.get('college')
    request.session['college'] = college
    
    return redirect("search_home")

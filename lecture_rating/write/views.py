from django.shortcuts import render,redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.contrib.auth.models import *
from main.models import *
from . form import LectureRatingBoard_Post
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Subquery

# Create your views here.
def write(request):
    pk=request.GET['lecture_id']
    lecture = Lecture.objects.get(lecture_id=pk)
    name= lecture.name 
    return render(request, 'write/write.html',{'name':name,'pk':pk})

def LectureRatingBoard_Post2(request):
    if request.method =='POST':
        form = LectureRatingBoard_Post(request.POST)
        if form.is_valid():
            post = form.save()

    else:
        form =  LectureRatingBoard_Post()
        return render(request, "write/write.html", {"form" : form})  
    


@csrf_exempt
def create(request):
    # user = User.objects.get(userid = request.GET['user'])
    # lecture = Lecture.objects.get(name = request.GET['lecture'])
    pk= request.POST['pk']
    lectureRatingBoard = LectureRatingBoard()
    lectureRatingBoard.username = request.user
    lectureRatingBoard.lecture = Lecture.objects.get(lecture_id=pk)
    lectureRatingBoard.tilte =  request.POST['title']
    lectureRatingBoard.content =  request.POST['content']
    year = request.POST['semesteryear']
    date = datetime.datetime(int(year), 3, 2)
    lectureRatingBoard.semester_year = date
    lectureRatingBoard.semester= request.POST
    lectureRatingBoard.pro_lecturePower = request.POST['pro_lecturePower']
    lectureRatingBoard.test_level = request.POST['test_level']
    lectureRatingBoard.project = request.POST['project']
    lectureRatingBoard.homework= request.POST['homework']
    lectureRatingBoard.stars = request.POST['stars']
    lectureRatingBoard.save()
    return redirect('lecture_detail', pk)
    
def home(request):
    lectureRatingBoards=LectureRatingBoard.objects
    return render(request, 'write/home.html', {'lectureRatingBoards':lectureRatingBoards})

def modify(request, pk):
    lectureRatingBoard_pk = pk
    lecture = Lecture.objects.get(lecture_id=lectureRatingBoard_pk)
    lectureRatingBoard = LectureRatingBoard.objects.get(lecture=lecture)
    name= lecture.name 
    context = {"lectureRatingBoard" : lectureRatingBoard, 'name':name, 'pk' : lectureRatingBoard_pk}
    return render(request, 'write/modify.html', context)

def detail(request,pk):
    lecture_detail = get_object_or_404(LectureRatingBoard,pk=pk)
    return render(request, 'write/detail.html', {'lecture_detail':lecture_detail})    

def update(request, pk):
    lectureRatingBoard = get_object_or_404(LectureRatingBoard, pk=pk)
    lectureRatingBoard.tilte =  request.POST['title']
    lectureRatingBoard.content =  request.POST['content']
    year = request.POST['semesteryear']
    date = datetime.datetime(int(year), 3, 2)
    lectureRatingBoard.semester_year = date
    lectureRatingBoard.semester= request.POST
    lectureRatingBoard.pro_lecturePower = request.POST['pro_lecturePower']
    lectureRatingBoard.test_level = request.POST['test_level']
    lectureRatingBoard.project = request.POST['project']
    lectureRatingBoard.homework= request.POST['homework']
    lectureRatingBoard.stars = request.POST['stars']
    lectureRatingBoard.save()
    lec = lectureRatingBoard.lecture
    return redirect('lecture_detail', lec.lecture_id)

    # lectureRatingBoard = get_object_404(LectureRatingBoard, pk=pk)
    # form = New_LectureRatingBoard(request.GET, instance=lectureRatingBoard)
    # if request.method =='POST':
    #     form = LectureRatingBoard_Post(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form =  LectureRatingBoard_Post()
    #     return render(request, 'write/modify.html')  

   
    
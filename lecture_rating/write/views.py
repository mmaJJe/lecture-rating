from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import *
from .models import *
from . form import LectureRatingBoard_Post

# Create your views here.
def write(request):
    return render(request, 'write.html')

def LectureRatingBoard_Post(request):

    if request.method =='POST':
        form = LectureRatingBoard_Post(request.POST)
        if form.is_valid():
            post = form.save()

    else:
        form =  LectureRatingBoard_Post()
        return render(request,)  
    

def create(request):
    user = User.objects.get(userid = request.GET['user'])
    lecture = Lecture.objects.get(name = request.GET['lecture'])
    lectureRatingBoard = LectureRatingBoard()
    lectureRatingBoard.user = user
    lectureRatingBoard.lecture = lecture
    lectureRatingBoard.tilte =  request.GET['title']
    lectureRatingBoard.content =  request.GET['content']
    lectureRatingBoard.save()
    
def home(request):
    lectureRatingBoards=LectureRatingBoard.objects
    return render(request, 'home.html', {'lectureRatingBoards':lectureRatingBoards})

def modify(request):
    return render(request, 'modify.html')

def detail(request,pk):
    lecture_detail = get_object_or_404(LectureRatingBoard,pk=pk)
    return render(request, 'detail.html', {'lecture_detail':lecture_detail})    

def update(request, pk):
    lectureRatingBoard = get_object_404(LectureRatingBoard, pk=pk)
    form = New_LectureRatingBoard(request.GET, instance=lectureRatingBoard)
    if request.method =='POST':
        form = LectureRatingBoard_Post(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =  LectureRatingBoard_Post()
        return render(request,)  

   
    
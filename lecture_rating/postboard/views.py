from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from main.models import University, Professor, Lecture, LectureRatingBoard



def postdetail(request, id):
    content = get_object_or_404(LectureRatingBoard, pk=id)
    context = {"content" : content}
    return render(request, "postboard/post_detail.html", context)


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from main.models import University, Professor, Lecture, LectureRatingBoard


def board(request):
    lec_list = LectureRatingBoard.objects.all()
    paginator = Paginator(lec_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context= {'lec_li':lec_list, 'posts':posts,}
    return render(request, 'postboard/main_board.html', context)

def postdetail(request, id):
    content = get_object_or_404(LectureRatingBoard, pk=id)
    context = {"content" : content}
    return render(request, "postboard/post_detail.html", context)


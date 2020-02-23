from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),
    path('detail/<int:id>', views.postdetail, name="postdetail"),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('write/', views.write, name="write"),
    path('modify/<int:pk>', views.modify, name="modify"),
    path('update/<int:pk>',views.update , name ="update"),
    path('write/create',views.create, name="create"),
    path('write/detail/<int:pk>',views.detail, name="detail"),
    path('write/newLecture',views.LectureRatingBoard_Post2, name="newLecture"),
]

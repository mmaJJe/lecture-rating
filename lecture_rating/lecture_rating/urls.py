from django.contrib import admin
from django.urls import path
import write.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', write.views.home, name="home"),
    path('write/', write.views.write, name="write"),
    path('modify/', write.views.modify, name="modify"),
    path('update/<int:pk>',write.views.update , name ="update"),
    path('write/create',write.views.create, name="create"),
    path('write/<int:pk>',write.views.detail, name="detail"),
    path('write/newLecture',write.views.LectureRatingBoard_Post, name="newLecture"),
]

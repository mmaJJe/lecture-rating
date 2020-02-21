from django.contrib import admin
from .models import LectureRatingBoard, Lecture, Professor, University

admin.site.register(LectureRatingBoard)
admin.site.register(Lecture)
admin.site.register(Professor)
admin.site.register(University)

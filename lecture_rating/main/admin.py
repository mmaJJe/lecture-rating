from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(University)
admin.site.register(Professor)
# Profile 추가 User 대용
admin.site.register(Profile)
admin.site.register(LectureRatingBoard)
admin.site.register(Lecture)

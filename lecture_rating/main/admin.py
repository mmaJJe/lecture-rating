from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(University)
admin.site.register(Professor)
admin.site.register(User)
admin.site.register(LectureRatingBoard)
admin.site.register(Lecture)
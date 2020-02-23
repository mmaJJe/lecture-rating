from django.contrib import admin
<<<<<<< HEAD
from .models import *
# Register your models here.


admin.site.register(University)
admin.site.register(Professor)
admin.site.register(User)
admin.site.register(LectureRatingBoard)
admin.site.register(Lecture)
=======
from .models import LectureRatingBoard, Lecture, Professor, University

admin.site.register(LectureRatingBoard)
admin.site.register(Lecture)
admin.site.register(Professor)
admin.site.register(University)
>>>>>>> f50cc25898a022f1f801863ae96e5d54e1ed94ec

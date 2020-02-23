from django.contrib import admin
from .models import *

admin.site.register(University)
admin.site.register(Professor)
admin.site.register(Lecture)
admin.site.register(User)
admin.site.register(LectureRatingBoard)

# Register your models here.

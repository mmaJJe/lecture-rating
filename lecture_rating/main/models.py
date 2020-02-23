<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> eab2a96b65da238a28c24a86b0378f07d415d786
from django.db import models
import random
import string

# Create your models here.

class University(models.Model) :
    name = models.CharField(max_length=20)
<<<<<<< HEAD
    def __str__ (self) :
=======
    def __str__(self):
>>>>>>> eab2a96b65da238a28c24a86b0378f07d415d786
        return self.name

class Professor(models.Model) :
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
<<<<<<< HEAD
    def __str__ (self) :
        return self.name

=======
    def __str__(self):
        return self.name


>>>>>>> eab2a96b65da238a28c24a86b0378f07d415d786
class Lecture (models.Model) :
    lecture_id = models.CharField(primary_key=True, max_length=20, default=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(8)))
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
<<<<<<< HEAD
    reco = models.IntegerField(default=0)
    not_reco = models.IntegerField(default=0)
    def __str__ (self) :
        return self.name

# class User(settings.AUTH_USER_MODEL) :
#     admission = models.DateField(blank=True, null=True)
#     university = models.ForeignKey(University, on_delete=models.CASCADE)
#     major = models.CharField(blank=True)

class LectureRatingBoard(models.Model) :
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    semester_year = models.DateField(blank=True, null=True)
    semester = models.CharField(max_length=5, blank=True, null=True)
    pro_lecturePower = models.IntegerField(default=0)
    test_level = models.IntegerField(default=0)
    project = models.IntegerField(default=0)
    homework = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.lecture.name
=======
    def __str__(self):
        return self.name

class User(models.Model) :
    userid = models.CharField(max_length=20, primary_key=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    student_number = models.CharField(max_length=20)
    def __str__(self):
        return self.userid

class LectureRatingBoard(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    def __str__(self):
        return self.title
>>>>>>> eab2a96b65da238a28c24a86b0378f07d415d786

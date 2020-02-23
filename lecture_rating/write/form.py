from django import forms
from main.models import LectureRatingBoard

class LectureRatingBoard_Post(forms.ModelForm):
    class Meta :
        model = LectureRatingBoard
        fields = ['username','lecture','title','content']
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('college/', views.find_college, name="find_college"),
    path('college/choose/', views.choose_college, name="choose_college"),
    path('search/lecture/', views.search_lecture, name="search_lecture")
]

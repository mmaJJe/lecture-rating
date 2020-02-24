from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('college/', views.find_college, name="find_college"),
    path('college/choose/', views.choose_college, name="choose_college"),
    path('search/lecture/', views.search_lecture, name="search_lecture"),
    path('search/home/', views.search_home, name="search_home"),
<<<<<<< HEAD
    path('search/write',views.write, name="write"),
    path('search/create', views.create, name="create")

=======
>>>>>>> 1b444d93fe8baf4eea963481ea20a5a20242a254
]

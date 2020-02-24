from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.postdetail, name="postdetail"),
    path('delete/<int:pk>/', views.delete, name='delete'),
]

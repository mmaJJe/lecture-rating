<<<<<<< HEAD
"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),
    path('postboard/', include('postboard.urls')),
=======
from django.contrib import admin
from django.urls import path
import write.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', write.views.home, name="home"),
    path('write/', write.views.write, name="write"),
    path('modify/', write.views.modify, name="modify"),
    path('update/<int:pk>',write.views.update , name ="update"),
    path('write/create',write.views.create, name="create"),
    path('write/<int:pk>',write.views.detail, name="detail"),
    path('write/newLecture',write.views.LectureRatingBoard_Post, name="newLecture"),
>>>>>>> eab2a96b65da238a28c24a86b0378f07d415d786
]

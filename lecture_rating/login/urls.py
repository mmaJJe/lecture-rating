"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views
urlpatterns = [
    path('',views.login ,name="login"),
    path('signup/',views.signup ,name="signup"),
    path('logout/', views.logout, name='logout')
]

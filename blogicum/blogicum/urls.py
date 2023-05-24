from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'), name='pages'),
    path('', include('blog.urls'), name='blog'),
]

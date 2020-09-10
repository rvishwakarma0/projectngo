from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home/', include('home.urls')),
    path('student/', include('student.urls')),
    path('member/', include('member.urls')),
    #path('homework/', include('homework.urls')),
    path('attendance/', include('attendance.urls')),

]

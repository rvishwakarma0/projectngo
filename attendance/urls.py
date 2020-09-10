from django.urls import path
from . import views

app_name="attendance"
urlpatterns = [

#path('attendance/',views.attendance,name="mark_attendance"),
#path('storeattend/',views.storeattend,name="store_attendance"),
path('markattendance/',views.MArkAttendance,name="mark_attendance"),
path('viewattendance/',views.viewattendance,name="view_attendance"),

]

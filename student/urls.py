from django.urls import path
from student import views

app_name = 'student'
urlpatterns = [
path('registration/',views.registration,name="student_registration"),
path('student_details/',views.student_details,name="student_details"),
]

from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from student.models import StudentData
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def atgetname(r):
    q = "attendance["+str(r)+"]"
    return q


def MArkAttendance(request):
    student_list = StudentData.objects.order_by("rollno")
    if request.method == 'POST':
        for student in student_list:
             var_t = atgetname(student.rollno)
             status=request.POST.get(var_t)
             try:
                 Attendance.objects.get(roll = student.rollno,date = datetime.date.today())
                 error_msg = "already submitted"
                 break
             except ObjectDoesNotExist:
                 Attendance.objects.create(roll = student, status = status)
                 error_msg = "successfully submited"
        return render(request,'attendance/markattendance.html',{'student_list':student_list,'error_msg':error_msg})


    else :

        return render(request,'attendance/markattendance.html',{'student_list':student_list})

def viewattendance(request):
    if request.method == 'POST':
        sdate=request.POST.get('sdate')
        ldate=request.POST.get('ldate')
        attend_list = Attendance.objects.filter(date__range=[sdate, ldate])
        return render(request,'attendance/viewattend.html',{'data':attend_list})
    else:
        return render(request,'attendance/viewattend.html')

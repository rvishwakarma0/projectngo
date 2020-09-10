from django.shortcuts import render,redirect
from .models import StudentData
from student.forms import StudentDataForm



def registration(request):
    form=StudentDataForm()
    if request.method == 'POST':
        form = StudentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(student_details)
        else:
            form=StudentDataForm()
    return render(request,'student/registration.html',{'forms':form})



def student_details(request):
    details = StudentData.objects.all()
    return render(request,'student/StudentDetails.html',{'details':details})

# def create_group(request):

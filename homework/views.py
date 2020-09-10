'''

from django.shortcuts import render

# Create your views here.



def homework(request):
    if request.method == 'POST':
        homw = GroupHomework()
        homw.Hgroup = request.POST.get('hid')
        homw.hwstatus = request.POST.get('hstatus')
        if 'hpic' in request.FILES:
            homw.homework = request.FILES['hpic']
        homw.save()
        return render(request,'/member/')
    else:
        hw = GroupHomework.objects.latest('id')
        return render(request,'member/homework.html',{'hw':'hw'})

def creategroup(request):
    if request.method == 'POST':
        crgp = GroupStudents()
        crgp.Sgroup = request.POST.get['gname']
        crgp.Greg = request.POST.get['gstudno']
        crgp.save()
        return render(request,"/member/")
    else:
        return render(request,'/member/creategroup.html')


'''

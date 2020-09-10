from django.shortcuts import render,redirect
from django.http import HttpResponse
from member.forms import MemberForm, MemberInfoForm

def index(request):
    mform = MemberForm()
    miform = MemberInfoForm()
    return render(request,'home/index.html',{'user_form':mform,'profile_form':miform})

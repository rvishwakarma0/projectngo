from django.shortcuts import render,redirect
from .forms import MemberForm, MemberInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'member/index.html')


@login_required
def userlogout(request):
    logout(request)
    return render(request,'member/logout.html')


def register(request):
    registered = False
    if request.method == 'POST':
        mform = MemberForm(data=request.POST)
        miform = MemberInfoForm(data=request.POST)
        if mform.is_valid() and miform.is_valid():
            user=mform.save()
            user.set_password(user.password)
            user.save()
            profile = miform.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print("found it")
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(mform.errors,miform.errors)
    else:
        mform = MemberForm()
        miform = MemberInfoForm()
    return render(request,'member/register.html',{'user_form':mform,'profile_form':miform,'registered':registered})



def userlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request,user)
        return redirect('/member/')
    else:
        return render(request,'home/index.html',{'error_msg':'Invalid login detail given.'})

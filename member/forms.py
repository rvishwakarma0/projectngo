from django import forms
from member.models import Member
from django.contrib.auth.models import User


class MemberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')


class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('profile_pic','college','address','city')

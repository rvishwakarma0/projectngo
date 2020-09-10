from django.db import models
from django.contrib.auth.models import User



class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank='True')
    college = models.CharField(max_length = 250)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username

'''
class MemberSchedule(models.Model):
    mem = models.ForeignKey(Member,on_delete=models.CASCADE)
    days = [
        ('1', 'monday'),
        ('2', 'tuesday'),
        ('3', 'wednesday'),
        ('4', 'thursday'),
        ('5', 'friday'),
        ('6', 'saturday'),
        ('7', 'sunday')
    ]
    day = models.CharField(max_length=1, choices = days,default= 7 )
    def _str_(self):
        return self.day

class MemberContribution(models.Model):
    memberid = models.ForeignKey(Member,on_delete=models.CASCADE)
    contri = models.IntegerField(default=0)
'''

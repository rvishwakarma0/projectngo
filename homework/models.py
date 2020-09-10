'''


from django.db import models
import datetime



class GroupHomework(models.Model):
    Hgroup = models.ForeignKey(GroupStudents,on_delete=models.CASCADE)
    homework = models.ImageField(upload_to='homework',blank='True')
    hwstatus = models.BooleanField(default=False)

'''

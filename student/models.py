from django.db import models

clas_choices = [
    (1, 1), (2, 2),(3, 3),(4, 4), (5, 5),(6, 6),(7, 7), (8,8), (9,9),(10,10),(11,11), (12,12),
]
class StudentData(models.Model):
    rollno = models.CharField(max_length=4,primary_key=True)
    pic = models.ImageField(upload_to="student_profile_pics",blank="False")
    #sgroup = models.ForeignKey(GroupInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank="False")
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=500)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    school = models.CharField(max_length=250)
    sclass = models.IntegerField(choices = clas_choices, default='5',blank="False")

    def _str_(self):
        return self.rollno
'''
class GroupStudents(models.Model):
    gid = models.CharField(max_length=2, primary_key=True)
    gname = models.CharField(max_length=100)
    def _str_(self):
        return self.gname
'''

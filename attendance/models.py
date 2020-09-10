from django.db import models
from student.models import StudentData
import datetime


class Attendance(models.Model):
    roll = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today)
    status = models.BooleanField(default="False")

from django.forms import ModelForm
from student.models import StudentData

class StudentDataForm(ModelForm):
    class Meta:
        model = StudentData
        fields = "__all__"

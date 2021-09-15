from django import forms
from .models import Student,Department,Lecturer



class Departmentform(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
 



class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class Lecturerform(forms.ModelForm):
    class Meta:
        model=Lecturer
        fields='__all__'
        widgets={
            'department':forms.CheckboxSelectMultiple()
        }
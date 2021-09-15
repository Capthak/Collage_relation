from django.db import models



class Department(models.Model):
    depname=models.CharField(max_length=500)
    depintake=models.IntegerField()

    def __str__(self):
        return self.depname

class Lecturer(models.Model):
    department=models.ManyToManyField(Department)
    lecname=models.CharField(max_length=100)
    lecsal=models.FloatField()
    lecsub=models.CharField(max_length=30)
    
    def written_by(self):
        return ",".join([str(p) for p in self.department.all()])
    
    def __str__(self):
        return self.lecname

class Student(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    stuname=models.CharField(max_length=50)
    sturollno=models.IntegerField()
    stuaddress=models.CharField(max_length=100)
    stumarks=models.IntegerField()

    def __str__(self):
        return self.stuname



from django.db import models


# Create your models here.
class Administrator(models.Model):
    name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    mail = models.CharField(max_length=20)
    code_admin = models.CharField(max_length = 20)

class Course(models.Model):
    name = models.CharField(max_length=20)
    code_course = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    code_teacher = models.CharField(max_length=20)
    admin = models.ForeignKey(Administrator,null=False,blank=False,on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher,null=False,blank=False,on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def nameStudent(self):
        txt = "{0} {1}"
        return txt.format(self.name,self.last_name)

class Parent(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)




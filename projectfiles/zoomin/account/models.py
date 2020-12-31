from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    num_id = models.CharField(max_length=30)


    def __str__(self):
        return self.user.username




class Course(models.Model):
    name = models.CharField(max_length=20)
    code_course = models.CharField(max_length=20)





class board_school(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('topic',max_length=100, blank=False, null=False)
    description = models.TextField('Description', max_length=300, blank=True , null=True)
    publication_date = models.DateField(default=date.today())

    class Meta:
        verbose_name = 'Board_school'
        verbose_name_plural = 'Board_school'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic


class board_class(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('topic',max_length=100, blank=False, null=False)
    description = models.TextField('Description', max_length=300, blank=True , null=True)
    publication_date = models.DateField(default=date.today())
    class Meta:
        verbose_name = 'Board_class'
        verbose_name_plural = 'Board_class'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic






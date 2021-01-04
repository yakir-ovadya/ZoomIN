from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30,null=True,blank=True)
    Last_Name = models.CharField(max_length=30,null=True,blank=True)
    Code = models.CharField(max_length=30,null=True,blank=True)
    ID_Number = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):
        return str(self.user)


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


class schedule_mod(models.Model):
    id = models.AutoField(primary_key=True)
    friday = models.CharField(max_length=100, blank=False, null=False)
    friday_link = models.CharField(max_length=100, blank=False, null=False)
    thursday = models.CharField(max_length=100, blank=False, null=False)
    thursday_link = models.CharField(max_length=100, blank=False, null=False)
    wednesday = models.CharField(max_length=100, blank=False, null=False)
    wednesday_link = models.CharField(max_length=100, blank=False, null=False)
    tuesday = models.CharField(max_length=100, blank=False, null=False)
    tuesday_link = models.CharField(max_length=100, blank=False, null=False)
    monday = models.CharField(max_length=100, blank=False, null=False)
    monday_link = models.CharField(max_length=100, blank=False, null=False)
    sunday = models.CharField(max_length=100, blank=False, null=False)
    sunday_link = models.CharField(max_length=100, blank=False, null=False)
    time = models.CharField(max_length=100, blank=False, null=False)
    topics = [friday, friday_link, thursday, thursday_link, wednesday, wednesday_link,
              tuesday, tuesday_link, monday, monday_link, sunday, sunday_link, time]

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return self.topics
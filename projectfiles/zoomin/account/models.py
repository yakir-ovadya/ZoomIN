from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField('שם פרטי', max_length=30, null=True, blank=True)
    Last_Name = models.CharField('שם משפחה', max_length=30, null=True, blank=True)
    Code = models.CharField('קוד הרשאה', max_length=30, null=True, blank=True)
    ID_Number = models.CharField('תעודת זהות', max_length=30, null=True, blank=True)
    in_class_op = (('נוכח', "נוכח"), ('לא נוכח', "לא נוכח"))
    in_class = models.CharField('סטטוס', choices=in_class_op, default='לא נוכח', max_length=300, null=True)

    pro1 = models.CharField('חשבון',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro2 = models.CharField('היסטוריה',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro3 = models.CharField('תנ"ך',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro4 = models.CharField('גאוגרפיה',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro5 = models.CharField('לשון',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro6 = models.CharField('ספרות',max_length=30,default='לא ניתן ציון', null=True, blank=True)
    pro7 = models.CharField('ספורט',max_length=30,default='לא ניתן ציון', null=True, blank=True)


    class Meta:
        verbose_name_plural = "userprofile"

    def __str__(self):
        return str(self.user)



class board_school(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('נושא',max_length=100, blank=False, null=False)
    description = models.TextField('תיאור', max_length=300, blank=True , null=True)
    publication_date = models.DateField('תאריך',default=str(date.today()))

    class Meta:
        verbose_name = 'Board_school'
        verbose_name_plural = 'Board_school'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic


class board_class(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('נושא',max_length=100, blank=False, null=False)
    description = models.TextField('תיאור', max_length=300, blank=True , null=True)
    publication_date = models.DateField('תאריך',default=str(date.today()))
    class Meta:
        verbose_name = 'Board_class'
        verbose_name_plural = 'Board_class'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic


class schedule_mod(models.Model):
    id = models.AutoField(primary_key=True)
    friday = models.CharField('יום שישי',max_length=100, blank=False, null=False)
    friday_link = models.CharField('קישור-יום שישי',max_length=100, blank=False, null=False)
    thursday = models.CharField('יום חמישי',max_length=100, blank=False, null=False)
    thursday_link = models.CharField('קישור-יום חמישי',max_length=100, blank=False, null=False)
    wednesday = models.CharField('יום רביעי',max_length=100, blank=False, null=False)
    wednesday_link = models.CharField('קישור-יום רביעי',max_length=100, blank=False, null=False)
    tuesday = models.CharField('יום שלישי',max_length=100, blank=False, null=False)
    tuesday_link = models.CharField('קישור-יום שלישי',max_length=100, blank=False, null=False)
    monday = models.CharField('יום שני',max_length=100, blank=False, null=False)
    monday_link = models.CharField('קישור-יום שני',max_length=100, blank=False, null=False)
    sunday = models.CharField('יום ראשון',max_length=100, blank=False, null=False)
    sunday_link = models.CharField('קישור-יום ראשון',max_length=100, blank=False, null=False)
    time = models.CharField('שעה',max_length=100, blank=False, null=False)
    topics = [friday, friday_link, thursday, thursday_link, wednesday, wednesday_link,
              tuesday, tuesday_link, monday, monday_link, sunday, sunday_link, time]

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return self.topics

class Test_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    profession = models.CharField('מקצוע',max_length=100, blank=False, null=False)
    date = models.DateField('תאאריך',default=str(date.today()), blank=True , null=True)
    start_time = models.CharField('שעת התחלה',max_length=30,default='09:00', null=True, blank=True)
    end_time = models.CharField('שעת סיום',max_length=30,default='11:00', null=True, blank=True)
    class Meta:
        verbose_name = 'Test_Schedule'
        verbose_name_plural = 'Test_Schedule'
        ordering = ['date']


    def __str__(self):
        return self.profession


class Presence_mod(models.Model):
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField("שם פרטי", max_length=30, null=True, blank=True)
    Last_Name = models.CharField("שם משפחה", max_length=30, null=True, blank=True)
    exist = models.BooleanField("נוכח", default=False)
    not_exist = models.BooleanField("לא נוכח", default=False)
    date = models.DateField("תאריך", default=str(date.today()), blank=True , null=True)
    profession = models.CharField("מקצוע", max_length=30, null=True, blank=True)
    hour = models.TimeField("שעה", auto_now=False, auto_now_add=False, null=True)
    val = [First_Name, Last_Name, exist, not_exist, date, profession, hour]

    class Meta:
        verbose_name = 'presence'
        verbose_name_plural = 'presence'

    def __str__(self):
        return self.val


from django.contrib import admin
from account.models import Administrator,Teacher,Student,Parent,Course
# Register your models here.


admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
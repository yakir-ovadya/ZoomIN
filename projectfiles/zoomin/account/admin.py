from django.contrib import admin
from account.models import Administrator,Teacher,Student,Parent,Course,board_school, board_class
# Register your models here.


admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
admin.site.register(board_school)
admin.site.register(board_class)
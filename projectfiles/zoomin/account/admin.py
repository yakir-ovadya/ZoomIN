from django.contrib import admin
from .models import board_school, board_class, UserProfile, schedule_mod, Test_Schedule
# Register your models here.

"""
admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
"""
admin.site.register(board_school)
admin.site.register(board_class)
admin.site.register(UserProfile)
admin.site.register(schedule_mod)
admin.site.register(Test_Schedule)
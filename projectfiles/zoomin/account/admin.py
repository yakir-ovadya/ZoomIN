from django.contrib import admin
from account.models import board_school, board_class,UserProfile
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
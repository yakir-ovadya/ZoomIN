from django.contrib import admin
from .models import board_school, board_class, UserProfile, schedule_mod, Test_Schedule, Presence_mod
# Register your models here.

"""
admin.site.register(Administrator)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
"""
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","First_Name","Last_Name","Code","ID_Number",)

admin.site.register(UserProfile, ProfileAdmin)

admin.site.register(board_school)
admin.site.register(board_class)
admin.site.register(Presence_mod)
admin.site.register(schedule_mod)
admin.site.register(Test_Schedule)
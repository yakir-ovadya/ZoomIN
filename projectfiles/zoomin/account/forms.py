from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import board_class, board_school, UserProfile, schedule_mod, Test_Schedule, Presence_mod


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.First_Name = self.cleaned_data['First_Name']
            user.Fast_Name = self.cleaned_data['Last_Name']

            if commit:
                user.save()
            return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('First_Name', 'Last_Name', 'Code', 'ID_Number')


class board_classForm(forms.ModelForm):
    class Meta:
        model = board_class
        fields = ['topic','description','publication_date']


class board_schoolForm(forms.ModelForm):
    class Meta:
        model = board_school
        fields = ['topic', 'description','publication_date']


class Schedule_Form(forms.ModelForm):
    class Meta:
        model = schedule_mod
        fields = ['friday', 'friday_link', 'thursday', 'thursday_link', 'wednesday', 'wednesday_link',
                  'tuesday', 'tuesday_link', 'monday', 'monday_link', 'sunday', 'sunday_link', 'time']

class Test_ScheduleCheck(forms.ModelForm):
    class Meta:
        model = Test_Schedule
        fields = ['profession', 'date','start_time', 'end_time']

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)


class Presence_form(forms.ModelForm):
    class Meta:
        model = Presence_mod
        fields = {'First_Name':'a', 'Last_Name':'a', 'exist':None, 'not_exist':None, 'date':None, 'hour':'a', 'profession':'a'}


class UserProfile_in_class(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('in_class',)


class UserProfile_grades(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('pro1','pro2','pro3','pro4','pro5','pro6','pro7',)
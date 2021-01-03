from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import board_class, board_school, UserProfile


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
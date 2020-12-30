from django import forms
from django.forms import ModelForm
from .models import board_class, board_school

class board_classForm(forms.ModelForm):
    class Meta:
        model = board_class
        fields = ['topic','description','publication_date']


class board_schoolForm(forms.ModelForm):
    class Meta:
        model = board_school
        fields = ['topic', 'description','publication_date']
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import board_schoolForm
from .models import board_school



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def grades(request):
    return render(request, 'grades.html')



def calendar(request):
    return render(request, 'calendar.html')

def presence(request):
    return render(request, 'presence.html')

def schedule(request):
    return render(request, 'schedule.html')

def Username_Recovery(request):
    return render(request, 'UsernameRecovery.html')

def bulletin_board_class(request):
    return render(request,'bulletin_board_class.html')

def bulletin_board(request):
    topics = board_school.objects.all()
    return render(request, 'bulletin_board.html',{'topics':topics})

def addBoardSchool(request):
    if request.method == 'POST':
        BoardSchool_form = board_schoolForm(request.POST)
        if BoardSchool_form.is_valid():
            BoardSchool_form.save()
            return redirect('bulletin_board')
    else:
        BoardSchool_form = board_schoolForm()
    return render(request,'add_bulletin_board.html',{'BoardSchool_form':BoardSchool_form})

def editBoardSchool(request,id):
    topics = board_school.objects.get(id=id)
    if request.method == 'GET':
        BoardSchool_form = board_schoolForm(instance=topics)
    else:
        BoardSchool_form = board_schoolForm(request.POST, instance=topics)
        if BoardSchool_form.is_valid():
            BoardSchool_form.save()
        return redirect('bulletin_board')
    return render(request, 'add_bulletin_board.html', {'BoardSchool_form': BoardSchool_form})

def deleteBoardSchool(request,id):
    topics = board_school.objects.get(id=id)
    topics.delete()
    return redirect('bulletin_board')


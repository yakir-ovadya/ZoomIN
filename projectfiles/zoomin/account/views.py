# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import Schedule_Form, board_schoolForm, UserProfileForm,ExtendedUserCreationForm, board_classForm
from .models import schedule_mod, board_school, board_class
# from django.contrib.auth.forms import UserCreationForm
# from .forms import ExtendedUserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from django.http import HttpResponse



def index(request):

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'

    return render(request, 'templates/home.html')


@login_required
def profile(request):
    return render(request,'home.html' )


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form': profile_form}
    return render(request, 'registration/signup.html', context)


def grades(request):
    return render(request, 'grades.html')


def calendar(request):
    return render(request, 'calendar.html')


def presence(request):
    return render(request, 'presence.html')


def schedule(request):
    topics = schedule_mod.objects.all()
    return render(request, 'schedule.html', {'topics': topics})


def Username_Recovery(request):
    return render(request, 'UsernameRecovery.html')


def bulletin_board_class(request):
    topics = board_class.objects.all()
    return render(request,'bulletin_board_class.html',{'topics':topics})


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

def addBoardClass(request):
    if request.method == 'POST':
        BoardClass_form = board_classForm(request.POST)
        if BoardClass_form.is_valid():
            BoardClass_form.save()
            return redirect('bulletin_board_class')
    else:
        BoardClass_form = board_classForm()
    return render(request,'add_bulletin_board_class.html',{'BoardClass_form':BoardClass_form})


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

def editBoardClass(request,id):
    topics = board_class.objects.get(id=id)
    if request.method == 'GET':
        BoardClass_form = board_classForm(instance=topics)
    else:
        BoardClass_form = board_classForm(request.POST, instance=topics)
        if BoardClass_form.is_valid():
            BoardClass_form.save()
        return redirect('bulletin_board_class')
    return render(request, 'add_bulletin_board_class.html', {'BoardClass_form': BoardClass_form})

def deleteBoardClass(request,id):
    topics = board_class.objects.get(id=id)
    topics.delete()
    return redirect('bulletin_board_class')

def deleteBoardSchool(request,id):
    topics = board_school.objects.get(id=id)
    topics.delete()
    return redirect('bulletin_board')

def addSchedule(request):
    if request.method == 'POST':
        schedule_form = Schedule_Form(request.POST)
        if schedule_form.is_valid():
            schedule_form.save()
            return redirect('schedule')
    else:
            schedule_form = Schedule_Form()
    return render(request, 'addschedule.html', {'schedule_form': schedule_form})


def editSchedule(request, id):
    topics = schedule_mod.objects.get(id=id)
    if request.method == 'GET':
        schedule_f = Schedule_Form(instance=topics)
    else:
        schedule_f = Schedule_Form(request.POST, instance=topics)
        if schedule_f.is_valid():
            schedule_f.save()
        return redirect('schedule')
    return render(request, 'addschedule.html', {'schedule_f': schedule_f})


def deleteSchedule(request,id):
    topics = schedule_mod.objects.get(id=id)
    topics.delete()
    return redirect('schedule')

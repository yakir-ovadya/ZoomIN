# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def grades(request):
    return render(request, 'grades.html')

def bulletin_board(request):
    return render(request, 'bulletin_board.html')

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
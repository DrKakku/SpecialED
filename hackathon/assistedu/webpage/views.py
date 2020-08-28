from django.shortcuts import render
from .models import *

def index(request):return render(
    request,
    'webpage/home.html',
    {
        'title':'HOME',
        'typeof':Disability.objects.all(),
        'name':Subject.objects.all(),
    },
)

def blind(request):return render(
    request,
    'webpage/blind.html',
    {
        'title':'Vision',
        'myurl':Disability.objects.all(),
        'name':Subject.objects.all(),
        
    }
)

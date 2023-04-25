from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def student(request):
    SFO=studentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=studentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is not Valid')
    return render(request,'students.html',d)

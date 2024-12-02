from django.shortcuts import render, reverse

from django.http import HttpResponseRedirect



def index(request):
    
    return render(request,'manager/index.html')
from django.shortcuts import render,redirect

def homePage(request):
    return render(request,'index.html')
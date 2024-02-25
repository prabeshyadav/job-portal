from django.shortcuts import render,redirect

def proxy(request):
    return render(request,'dashboard/dashboard.html')

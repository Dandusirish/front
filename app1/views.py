from django.shortcuts import render

# Create your views here.
def back(request):
    return render(request,'back.html')
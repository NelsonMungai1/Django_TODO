from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")
def temp(request):
    return render(request,'temp.html')
# VIEW is essential a function that returns a certain kind of Response
from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.

# Create your views here.
def stud(request):

    data = Student.objects.all()
    return HttpResponse(data)
    #return render(request,'index.html',{'data':data})


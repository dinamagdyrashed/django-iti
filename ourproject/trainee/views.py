from django.shortcuts import render
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
def alltrainee(request):
    context={}
    context['trainees']=Trainee.objects.all()
    # trainees=[[1,'John Doe'],[2,'Jane Smith'],[3,'Mike Johnson'],[4,'Emily Davis']]
    return render(request,'trainee/list.html',context)

def gettraineeid(request):
    return HttpResponse('<h1>Hello from id trainee</h1>')

def updatetrainee(request,id):
    return HttpResponse(f'<h1>Hello from update trainee {id}</h1>')

def inserttrainee(request):
    print(request.POST)
    if request.method=='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        image=request.FILES['trimage']
        Trainee.objects.create(name=name,email=email,image=image)
    return render(request,'trainee/insert.html')

def deletetrainee(request,id):
    return HttpResponse(f'<h1>trainee {id} deleted</h1>')
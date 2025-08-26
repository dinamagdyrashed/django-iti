from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Trainee
from track.models import Track
# Create your views here.
def alltrainee(request):
    context={}
    context['trainees']=Trainee.getalltrainees().order_by('id')
    # trainees=[[1,'John Doe'],[2,'Jane Smith'],[3,'Mike Johnson'],[4,'Emily Davis']]
    return render(request,'trainee/list.html',context)

def gettraineeid(request):
    return HttpResponse('<h1>Hello from id trainee</h1>')

def updatetrainee(request,id):
    trainee=Trainee.gettraineebyid(id)
    context={'trainee':trainee}
    context['tracks']=Track.getalltracks()
    if request.method=='POST':
        trainee.name=request.POST['trname']
        trainee.email=request.POST['tremail']
        trainee.trackid=Track.gettrackbyid(request.POST['trtrack'])
        if request.FILES.get('trimage'):
            trainee.image=request.FILES['trimage']
        trainee.save()
        # return HttpResponseRedirect('/Trainee/')
        return redirect('alltrainee')
    return render(request,'trainee/update.html',context)

def inserttrainee(request):
    print(request.POST)
    context={}
    context['tracks']=Track.getalltracks()
    if request.method=='POST':
        # trackid=request.POST['trtrack']
        # trackobj=Track.objects.get(id=trackid)
        Trainee.objects.create(name=request.POST['trname'],email=request.POST['tremail'],image=request.FILES['trimage'],trackid=Track.gettrackbyid(request.POST['trtrack']))
        return redirect('alltrainee')
    return render(request,'trainee/insert.html',context)

def deletetrainee(request,id):
    # Trainee.objects.filter(id=id).delete()
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('alltrainee')
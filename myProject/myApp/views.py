from django.shortcuts import get_object_or_404, redirect, render
from .form import EditPost
from .models import *

# Create your views here.
def loginPage(request):
    return render(request,'login.html')

def signupPage(request):
    return render(request,'signup.html')

def home(request):
    man=Person.objects.all()
    return render(request,'home.html',{'mans':man})

def dele(request, id):
    de=Person.objects.get(id=id)
    de.delete()
    return redirect('home')

def edit(request,id):
    ed=get_object_or_404(Person,id=id)
    if request.method=="POST":
        # form=EditPost(request.POST,instance=ed)
        form= EditPost(request.POST,request.FILES,instance=ed)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        context = {'form': EditPost(instance=ed), 'id': id}
        return render(request,'edit.html',context)
    return render(request,'edit.html',{'form':form})

def add(request):
    if request.method == "POST":
        form = EditPost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditPost()
    return render(request,'add.html',{"form":form})
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee

from .forms import EmpForm
from django.contrib import messages

# Create your views here.
def index(request):
   if request.method == 'POST':
      form = EmpForm(request.POST)
      if form.is_valid():
         form.save()
         emp=Employee.objects.all()
         return render(request,'emp/index.html',{'form':form,'emp':emp})
   else:
      form=EmpForm()
      emp=Employee.objects.all()
      return render(request,'emp/index.html',{'form':form,'emp':emp})

def update(request,id):
   a=Employee.objects.get(id=id)
   name=a.name
   pos=a.position
   salary=a.salary
   form=EmpForm(initial={'id':id,'name': name,'position':pos,'salary':salary})
   return render(request,'emp/edit.html',{'form':form})






def delete(request,id):
   a=Employee.objects.get(id=id)
   a.delete()
   return redirect('/')
   

  
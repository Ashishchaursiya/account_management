from django.shortcuts import render,redirect
from .forms import customerRegister
from .models import Customer
# Create your views here.
# add data
def Add(request):
    fm=customerRegister()
    if request.method=="POST":
        fm=customerRegister(request.POST)
        if fm.is_valid():
            fm.save()
        fm=customerRegister()   
        return render(request,"add.html",{'form':fm,'add':'xcdfg'}) 
    else:
        return render(request,"add.html",{'form':fm})    
             
   
#show and add data
def home(request):
    data=Customer.objects.all() 
    credit_sum=0
    due_sum=0
    for i in data:
        credit_sum=credit_sum+i.credit
        due_sum=due_sum+i.due
    if request.method=="POST":
        fm=customerRegister(request.POST)
        if fm.is_valid():
            fm.save()
        fm=customerRegister()   
        return render(request,"index.html",{"form":fm,'data':data,'add':'dfrtg'}) 
             
    else:
        fm=customerRegister() 
    return render(request,"index.html",{"form":fm,'data':data,"credit":credit_sum,'due':due_sum})
#delete data
def delete(request,id):
    if request.method=="POST":
        obj=Customer.objects.get(id=id)
        obj.delete()
        return redirect('/')


#updae data
def update(request,id):
    fm=customerRegister()
    if request.method=="POST":
        obj=Customer.objects.get(id=id)
        fm_obj=customerRegister(request.POST,instance=obj)
        if fm_obj.is_valid():
            fm_obj.save()
            return render(request,"update.html",{"form":fm,'update':'dfrtg'}) 
    else:          
        obj=Customer.objects.get(id=id)
         
    return render(request,"update.html",{"form":fm,"id":id})

#search data
def search(request):
    data=Customer.objects.all() 
    credit_sum=0
    due_sum=0
    for i in data:
        credit_sum=credit_sum+i.credit
        due_sum=due_sum+i.due
    try:
        query=request.GET.get("search")
    except:
        query=None 
    products=Customer.objects.filter(name__icontains=query) 
    
    return render(request,'index.html',{'data':products,"credit":credit_sum,'due':due_sum})

 


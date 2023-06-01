from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import SignupForm,Add_record
from .models import Record
# Create your views here.

def Home (request):
    records=Record.objects.all()
    
    #second
    if request.method=="POST":
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login (request,user)
            messages.success(request,'loging successful')
            return redirect ('home')
        else:
            messages.success(request,'error logining user')
            return redirect ('home')
    else:
            
     return render(request,'index.html',{'data':records})



def logout_user(request):
    logout(request)
    messages.success(request, 'you are logout, thanks once more')
    return redirect('home')

def reg_user(request):
    if request.method=="POST":
        form=SignupForm(request.POST);
        if form.is_valid():
            form.save()
            # i will authenticate the user
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
        
            login(request,user)
            messages.success(request,"Signup successful")
            return redirect('home')
    
    #if the  form is not post that means they are just perusing the form to see so we give them the form to fill
    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form}) 



def customer_record(request,pk):
    if request.user.is_authenticated:
        cust_record= Record.objects.get(id=pk)
        return render(request,'detail.html',{'data':cust_record})
    else:
         messages.success(request,"kpele you need to login first")
         return redirect('home')
    

def delete_record(request, pk):

    delete =Record.objects.get(id=pk)
    delete.delete()
    messages.success(request,"Record don delete now ")
       
    return redirect('home')
    
def add_record(request):
    data= Add_record(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if data.is_valid():
                add_record=data.save()
                messages.success(request,"Record don add now ")
    
                return redirect('home')  
        return render (request,'create.html',{'data':data})
    else:
        messages.success(request,"you are not authenicated  oo")
        return redirect('home') 
    
    
def update_record(request , pk):
    if request.user.is_authenticated:
        
        data= Record.objects.get(id=pk)
        newdata= Add_record(request.POST or None , instance= data)
        if newdata.is_valid():
             newdata.save()
             messages.success(request,"updated successfully  oo")
             return redirect('home') 
        else:
            return render(request,'update.html',{'data':newdata}) 
    else:
         messages.success(request,"you are not authenticate oo")
         return redirect('home')        
        


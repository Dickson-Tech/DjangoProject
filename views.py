from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from . models import User


# Create your views here.
def home(request):
    return render(request, "licenceapp/index.html")
def register(request): #function initiating the register task/operation
    if request.method =="POST": #request the register template so the operations should be performed
        username =request.POST.get('username') #username request to store the value that will be gotten from register html 
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        number=request.POST.get('number')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        password1=request.POST.get('password1')
        # Create a new patient entry in the database using the User model
        user = User(username=username,email=email,fname=fname,lname=lname,number=number,gender=gender,dob=dob,password1=password1) #user stores every objects into the database
        #user.firstname = fname
        #user.lastname =lname
        #user.email =email
        #user.number = number
        #user.gender =gender
        #user.dob = dob
        
        user.save() # Django generates and executes the necessary SQL queries to insert a new row into the user table with the values specified in the Patient instance.

        messages.success(request, "Your Account has been successfully created")   
        return redirect('login')
    return render(request, "Licenceapp/register.html") # tries to give back the actual actions as requested. 

    
def login(request):
     if request.method =="POST":
         username =request.POST.get('username')
         password1=request.POST.get('password1')

         user = authenticate(username=username,password1=password1)

         if user is not None:
             login(request,user)
             fname =user.first_name
             return render(request, "authentication/index.html", {'fname':fname})
             
         else:
             messages.error(request, "Invalid Credentials.")
             return redirect('application')

             
         
                
     return render(request, "Licenceapp/login.html")
    
def logout(request):
    pass #used as the placeholder in the function without affection the flow of execution

def home(request): 
    return render(request, 'Licenceapp/home.html')

def application(request):
    return render(request, 'Licenceapp/application.html')
 





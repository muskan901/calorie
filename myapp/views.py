from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from myapp.models import Contact
from myapp.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

# rVP30RiAbT1495IpGfetSMnoR5aMUq7MGtZqJvp5

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("home page")

def check(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'rVP30RiAbT1495IpGfetSMnoR5aMUq7MGtZqJvp5'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'check.html', {'api': api})
    else:
        
     return render(request,'check.html', {'query': 'Enter a valid query'})

def login(request):
    if request.method=="POST":
       username= request.POST['username'] 
       pass1= request.POST['pass1']     
       
       user = authenticate(username=username, password=pass1)    
       if user is not None:
           login(request,user)   
           return render(request,"index.html")
           
       else:
           messages.error(request,"Bad Credentials!")   
        #    return redirect('home')    
    
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # if pass1!=pass2:
        #     return HttpResponse("Your password and confirm password are not Same!!")
        #     # error='not same password'
        # else:
        signup=User(username=username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2, date=datetime.today())
        signup.save()
        messages.success(request,"Your account has been successfully created")
        return render(request,'login.html')
    
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email') 
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request,'contact.html')
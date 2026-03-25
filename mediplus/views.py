from django.shortcuts import render,HttpResponse,redirect
from mediplus.models import user_detailss,query
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        if email == 'admin@gmail.com' and password == 'admin':
            request.session['email']=email
            request.session['admin']='admin'
            return render(request,'adminindex.html',{'status':'admin login successful'})

        elif user_detailss.objects.filter(email=email,password=password).exists():
            userdetails=user_detailss.objects.get(email=request.POST['email'],password=password)
            if userdetails.password == request.POST['password']:
                request.session['uid']=userdetails.id
                request.session['uname']=userdetails.name
                request.session['uemail']=userdetails.email
                request.session['user']='user'
                messages.error(request, "user login successful")
                return render(request,'index.html')

        else:
            messages.error(request, "user login unsuccessful")
    return render(request,'login.html')  
  
    
def logout(request):
     session_key = list(request.session.keys())
     for key in session_key:
          del request.session[key]
     messages.error(request, "logout successful")
     return redirect(index)
        
    
#user registration view
def register(request):
    if request.method == 'POST':
        #fetch form data
        photo=request.FILES['photo']
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        #store in database
        #save data to database
        if user_detailss.objects.filter(email=email).exists():
            messages.error(request, "user already exist")
            return render(request,'register.html')
            
        else:
            User_det=user_detailss(photo=photo,name=name,email=email,phone=phone,password=password)
            User_det.save()
            messages.error(request, "registered successfully")
    return render(request,'register.html')

def queries(request):
    if request.method == 'POST':
        #fetch form data
        queryname=request.POST.get('queryname')
        queryemail=request.POST.get('queryemail')
        querymessage=request.POST.get('querymessage')
        #store in database
        query_det=query(queryname=queryname,queryemail=queryemail,querymessage=querymessage)
        #save data to database
        query_det.save()
        messages.error(request, "query added successfully'")
    return render(request,'index.html')
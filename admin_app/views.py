from django.shortcuts import render,HttpResponse,redirect
from mediplus.models import user_detailss,query
from admin_app.models import doctor_detailss
from user_app.models import appointment_details
from django.contrib import messages

# Create your views here.
def load_admin(request):
    return HttpResponse('admin app')

def user_det(request):
    #fetch all user details from database
    data=user_detailss.objects.all()
    #response to be sent to html page
    return render(request,'user_details.html',{'response':data})#'response' is the variable name to be used in html page to access data

def user_delete(request,id):
    user_data=user_detailss.objects.get(pk=id)
    user_data.delete()
    messages.error(request, "deleted successfully")
    return redirect(user_det)

def user_update(request,id):
    user_updt=user_detailss.objects.get(pk=id)
    return render(request,'user_update.html',{'result':user_updt})
    
def user_updates(request,id):
    if request.method == 'POST':
        photo=request.FILES['photo']
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        User_det=user_detailss(id=id,photo=photo,name=name,email=email,phone=phone,password=password)
        #save data to database
        User_det.save()
        messages.error(request, "updated successfully")
        return redirect(user_det)
    return render(request,'user_update.html')

def registerdoctor(request):
    if request.method == 'POST':
        #fetch form data
        doctorphoto=request.FILES['doctorphoto']
        doctorname=request.POST.get('doctorname')
        doctoremail=request.POST.get('doctoremail')
        doctorphone=request.POST.get('doctorphone')
        doctorpayment=request.POST.get('doctorpayment')
        doctorhours=request.POST.get('doctorhours')
        doctorspecialisation=request.POST.get('doctorspecialisation')
        #store in database
        Doc_det=doctor_detailss(doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorpayment=doctorpayment,doctorhours=doctorhours,doctorspecialisation=doctorspecialisation,)
        #save data to database
        Doc_det.save()
        messages.error(request, "registered successfully")
    return render(request,'adddoctor.html')

def doc_det(request):
    #fetch all user details from database
    doc_data=doctor_detailss.objects.all()
    #response to be sent to html page
    return render(request,'doctor_details.html',{'drs':doc_data})

def doctor_delete(request,id):
    doc_data=doctor_detailss.objects.get(pk=id)
    doc_data.delete()
    messages.error(request, "deleted successfully")
    return redirect(doc_det)

def doctor_update(request,id):
    doc_updt=doctor_detailss.objects.get(pk=id)
    return render(request,'doctor_update.html',{'dtrs':doc_updt})

def doctor_updates(request,id):
    if request.method == 'POST':
        doctorphoto=request.FILES['doctorphoto']
        doctorname=request.POST.get('doctorname')
        doctoremail=request.POST.get('doctoremail')
        doctorphone=request.POST.get('doctorphone')
        doctorpayment=request.POST.get('doctorpayment')
        doctorhours=request.POST.get('doctorhours')
        doctorspecialisation=request.POST.get('doctorspecialisation')
        Doc_det=doctor_detailss(id=id,doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorpayment=doctorpayment,doctorhours=doctorhours,doctorspecialisation=doctorspecialisation)
        #save data to database
        Doc_det.save()
        messages.error(request, "updated successfully")
        return redirect(doc_det)
    return render(request,'doctor_update.html')

def viewquery(request):
    #fetch all user details from database
    data=query.objects.all()
    #response to be sent to html page
    return render(request,'viewquery.html',{'response':data})

def app_view(request):
    #fetch all user details from database
    data=appointment_details.objects.all()
    #response to be sent to html page
    return render(request,'appointment_list.html',{'app':data})

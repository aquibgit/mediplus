from django.shortcuts import render,HttpResponse,redirect
from mediplus.models import user_detailss
from admin_app.models import doctor_detailss
from user_app.models import appointment_details
from django.contrib import messages
# Create your views here.
def load_user(request):
    return HttpResponse('user app')

def user_profile(request):
    user_id=request.session['uid']
    user_data=user_detailss.objects.get(pk=user_id)
    return render(request,'user_profile.html',{'result':user_data})

def book_app(request):
    doc_data=doctor_detailss.objects.all()
    user_id=request.session['uid']
    if request.method == 'POST':
        #fetch form data
        patient_name=request.POST.get('patient_name')
        patient_email=request.POST.get('patient_email')
        patient_phone=request.POST.get('patient_phone')
        patient_age=request.POST.get('patient_age')
        booking_date=request.POST.get('booking_date')
        doctor_name=request.POST.get('doctor_name')
        patient_problem=request.POST.get('patient_problem')
        #store in database
        app_det=appointment_details(user_id=user_id,patient_name=patient_name,patient_email=patient_email,patient_phone=patient_phone,patient_age=patient_age,booking_date=booking_date,doctor_name=doctor_name,patient_problem=patient_problem)
        #save data to database
        app_det.save()
        messages.error(request, "appointment successfull")
    return render(request,'appointment.html',{'doctors':doc_data})

def app_list(request):
    sid=request.session['uid']
    #fetch all user details from database
    data=appointment_details.objects.filter(user_id=sid)
    #response to be sent to html page
    return render(request,'appointment_list.html',{'app':data})

def app_delete(request,id):
    app_data=appointment_details.objects.get(pk=id)
    app_data.delete()
    messages.error(request, "deleted successfully")
    return redirect(app_list)

def app_update(request,id):
    doc_data=doctor_detailss.objects.all()
    app_updt=appointment_details.objects.get(pk=id)
    return render(request,'app_update.html',{'apps':app_updt,'doctors':doc_data})

def app_updates(request,id):
    user_id=request.session['uid']
    if request.method == 'POST':
        #fetch form data
        patient_name=request.POST.get('patient_name')
        patient_email=request.POST.get('patient_email')
        patient_phone=request.POST.get('patient_phone')
        patient_age=request.POST.get('patient_age')
        booking_date=request.POST.get('booking_date')
        doctor_name=request.POST.get('doctor_name')
        patient_problem=request.POST.get('patient_problem')
        #store in database
        app_det=appointment_details(id=id,user_id=user_id,patient_name=patient_name,patient_email=patient_email,patient_phone=patient_phone,patient_age=patient_age,booking_date=booking_date,doctor_name=doctor_name,patient_problem=patient_problem)
        #save data to database
        app_det.save()
        messages.error(request, "updated successfully")
        return redirect(app_list)
    return render(request,'appointment.html')
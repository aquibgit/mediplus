"""
URL configuration for mediplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('load_admin',views.load_admin),
    #url to display user details
    path('user_det',views.user_det),
    path('user_delete/<int:id>',views.user_delete,name="user_delete"),
    path('user_update/<int:id>',views.user_update,name="user_update"),
    path('user_update/user_updates/<int:id>',views.user_updates,name="user_updates"),
    path('registerdoctor',views.registerdoctor),
    path('doc_det',views.doc_det),
    path('doctor_delete/<int:id>',views.doctor_delete,name="doctor_delete"),
    path('doctor_update/<int:id>',views.doctor_update,name="doctor_update"),
    path('doctor_update/doctor_updates/<int:id>',views.doctor_updates,name="doctor_updates"),
    path('viewquery',views.viewquery),
    path('app_view',views.app_view),

]

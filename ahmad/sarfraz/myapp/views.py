from django.shortcuts import render,redirect
from .models import (Signup,Admission,User_login,Admin,Car_parking,
Library,Fee,Repeat_course,
Scholarship,
Scholarship_data
)
from .form import (signup,Admissionf,Myform,Adminf,Car_parkingf,
    Libraryf,Feef,Repeat_coursef,
    scholarshipf,
    scholarship_dataf,
    otp_form,
    Detail
    )
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from sarfraz import settings
from django.contrib import messages
from django .core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response
from myapp.serializer import Signup_serializer
@api_view(['POST','DELETE'])
def signup_api(request):
    sarfraz=Signup.objects.all()
    if request.method=="POST":
        my_serializer=Signup_serializer()
        if my_serializer.is_valid():
            my_serializer.save()
            return Respose(my_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=="DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)

# Email denotified  at line no :: 69 188,110,131,157,188,301
# Create your views here.

def empty(a,nn=0):
    for i in a:
        nn+=1
    del a[0:nn]
    return a   


import sqlite3
connection=sqlite3.connect('db.sqlite3',check_same_thread=False)
cursor=connection.cursor()        
otp_verification_variable=False

otp_list=[]
name_list=[]
email_list=[]
father_list=[]
phone_number_list=[]
password_list=[]
cnic_list=[]
variable_list=[3]
def first_url(request):
    form=signup()
    if request.method=="POST":
        form=signup(request.POST)
        if form.is_valid():
            empty(name_list)    #  WE defined a function to make a list empty before it gets another value 
            empty(email_list)
            empty(otp_list)  
            empty(password_list)
            empty(phone_number_list)
            empty(father_list)
            empty(cnic_list)
            name=request.POST['name']
            name_list.append(name)
            email=request.POST['email_address']
            email_list.append(email)
            father_name=request.POST['father_name']
            father_list.append(father_name)
            phone_number=request.POST['phone_number']
            phone_number_list.append(phone_number)
            password=request.POST['password']
            password_list.append(password)
            otp=random.randint(100000,999999)
            otp_list.append(otp)
            cnic=request.POST['cnic']
            cnic_list.append(cnic)
            print(otp)
            context={
                "form":name,
                "otp":otp
            }
            html_message=render_to_string('email.html',context)
            plain_message=strip_tags(html_message)
            my_subject="Account Verification"
            message=EmailMultiAlternatives(
                body=plain_message,
                from_email=None,
                subject=my_subject,
                to=[
                    email
                ]
            )
            check_list=[]
            query="select* from myapp_signup"
            cursor.execute(query)
            variable=cursor.fetchall()
            for i in variable:
                check_list.append(i[5])
            connection.commit()
            if cnic in check_list:
                messages.success(request,"This CNIC is already registered !! ")
            else:
                message.attach_alternative(html_message,"text/html")
                try:
                    message.send()
                    return redirect('otp/')
                except:    
                    return HttpResponse("<h1 align='center'>There is some problem please try again </h1>")    
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,"index.html",context)
def otp_template(request):
    form=otp_form()
    if request.method=="POST":
        form=otp_form(request.POST)
        if form.is_valid():
            name=request.POST['otp_variable']
            print(form.cleaned_data)
            try:
                if int(otp_list[0])==int(name):
                    Signup.objects.create(name=name_list[0],
                    father_name=father_list[0],
                    phone_number=phone_number_list[0],
                    email_address=email_list[0],
                    password=password_list[0],
                    cnic=cnic_list[0]
                    )
                    variable_list.insert(0,1)
                    messages.success(request,"Account created successfully !! ")
                    return redirect('signup/')
                else:
                    variable_list.insert(0,"sarfraz")
                    messages.success(request,"Incorrect OTP !! Try to resend ")
            except:
                messages.success(request,"There is some problem !!Please try again ")
    context={
        "form":form
    }        
    return render(request,"otp_template.html",context)        

def reverification(request):
    if variable_list[0]==1:
        return HttpResponse("<h2 align='center'>Your Account is already created !! You can now login !!</h2>")
    else:    
        try:
            otp=random.randint(100000,999999)
            empty(otp_list)
            otp_list.append(otp)
            print("reverified otp is ",otp)
            subject="Reverification of OTP "
            message="Dear  "+name_list[0]+ f", \n  Your One Time Password is {otp}"
            from_email=settings.EMAIL_HOST_USER
            to_list=[
            email_list[0]
            ]   
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            return HttpResponse(f"<h1 align='center'>We Just have sent an email to {email_list[0]} for reverification !!</h1> ")
        except:
            return HttpResponse("<h1 align='center'>There is some problem please try again !!</h3>")
def second_url(request):
    return render(request,"mainpage.html")  
def third_url(request):
    form=Admissionf()
    if request.method=="POST":
        form=Admissionf(request.POST,request.FILES)
        if form.is_valid():
            Admission.objects.create(**form.cleaned_data)

            # We are defining function to verify user by email 
            name=request.POST['name']
            email=request.POST['email_address']
            subject="Admission Application confirmation"
            message="Dear "+name+" \n Your application is submitted successfully to Islamia Universty of Bahawalpur"
            from_email=settings.EMAIL_HOST_USER
            to_list=[
                email
            ]
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            return HttpResponse("<h2 align='center'>Your request has been submitted Successfully. <br>You will soon receive a application  confirmation message from us  </h2>")
        else:
            print(form.errors)   
    context={
        "form":form
    }                
    return render(request,"admission.html",context)

def fourth_url(request):
    form=Myform()
    if request.method=="POST":
        form=Myform(request.POST)
        if form.is_valid():
            User_login.objects.create(**form.cleaned_data)
            # We are sending email to thats account to verify him 
            name=request.POST['name']
            email=request.POST['email_address']
            cnic=request.POST['cnic']
            print(cnic)
            check_list=[]
            query=f"select* from myapp_signup where cnic = '{cnic}' "
            cursor.execute(query)
            variable=cursor.fetchall()
            for i in variable:
                check_list.append(i[0])
                check_list.append(i[3])
                check_list.append(i[4])
                check_list.append(i[5])
            print(check_list)    
            if name in check_list and email in check_list and cnic in check_list :
                subject=" Login   verification "
                message="Dear "+name+", \n  You are loged in to Eportal Islamia Universty Of Bahawalpur  \n Thanks for visiting us again "
                from_email=settings.EMAIL_HOST_USER
                to_list=[
                    email
                ]
                send_mail(subject,message,from_email,to_list,fail_silently=False)
                return redirect('main/')
            else:
                messages.success(request,"No user with this data is registered  !!")
        else:
            print(form.errors) 
    context={
        "form":form
    }            
    return render(request,"login.html",context)    

def fifth_url(request):
    form=Adminf()
    if request.method=="POST":
        form=Adminf(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
        name1=request.POST['name']
        password1=request.POST['password']
        user=authenticate(username=name1,password=password1)

        # we are going to send an email to inform that another user is loged in your panel  
        if user  is not None:
            login(request,user)
            Admin.objects.create(**form.cleaned_data)
            name=request.POST['name']
            to_email=[('232323sarfrazsaleem@gmail.com')
            ]
            from_email=settings.EMAIL_HOST_USER
            subject="Admin Login notification"
            message="Dear admin Muhammad Sarfraz , \n A user named "+ f" '{name}' "  +"has been loged in to your admin panel  \n In case you have any objection about his loging in you can check your system to handle that "
            send_mail(subject,message,from_email,to_email,fail_silently=False)
            Admin.objects.create(**form.cleaned_data)
            print("Mail sent successfully ")
            return redirect('Admin/')
        else:
            return HttpResponse("<h1  align='center'><br><br><br><br><br>There is some problem in loging you in please try agian </h1>")    
    context={
        "form":form
    }
    return render(request,'admin.html',context)      

def car_parking(request):
    form=Car_parkingf()
    if request.method=="POST":
        form=Car_parkingf(request.POST,request.FILES)
        if form.is_valid():
            Car_parking.objects.create(**form.cleaned_data)
            return HttpResponse("<h2 align='center'>You Application has been submitted You will soon receive a message from us </h2>")
        else:
            print(form.errors)
    context={
        "form":form
        }
    return render(request,"car_parking.html",context)                  

def library(request):
    form=Libraryf()
    if request.method=="POST":
        form=Libraryf(request.POST)
        if form.is_valid():
            email=request.POST['email']
            name=request.POST['name']
            subject="Application Submission"
            message=f"Dear {name} your application for library card has been submitted successfully "
            from_email=settings.EMAIL_HOST_USER
            to_email=[
                email
            ]
            try:
                Library.objects.create(**form.cleaned_data)
                send_mail(subject,message,from_email,to_email,fail_silently=True)
            except:
                return HttpResponse("<h1>There is problem in In processing your request Please try again</h1>")    
            return HttpResponse("<h2 align='center'>Your request has been received you will soon receive a message from us </h2>")
        else:
            print(form.errors)
    context={
        "form":form
    }
    return render(request,"library.html",context)            

def fee(request):
    form=Feef()
    if request.method=="POST":
        form=Feef(request.POST,request.FILES)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            try:
                Fee.objects.create(**form.cleaned_data)
                subject="Fee Concession Application Verification"
                message=f"Dear  {name} Your application for fee concession has been submitted "
                from_email=settings.EMAIL_HOST_USER
                to_email=[
                    email
                    ]
                send_mail(subject,message,from_email,to_email,fail_silently=True)
                return HttpResponse("<h2 align='center'>Your application has been received You will soon receive a message from us </h2>")
            except:
                return HttpResponse("<h1 align='center'>There is some problem in.Please try again </h1>")    
        else:
            print(form.errors) 
    context={
        "form":form
    }           
    return render(request,"fee.html",context)    

def repeat_a(request):
    form=Repeat_coursef()
    if request.method=="POST":
        form=Repeat_coursef(request.POST,request.FILES)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            subject="Repeat Course Application "
            message=f"Dear  {name} Your application for Repeat course has been submitted "
            from_email=settings.EMAIL_HOST_USER
            to_email=[
                email
            ]
            try:
                send_mail(subject,message,from_email,to_email,fail_silently=True)
                Repeat_course.objects.create(**form.cleaned_data)
                return HttpResponse("<h1 align='center'>Your application has been submitted </h1>")
            except:    
                return HttpResponse("<h2 align='center'>Your request is submitted successsfully You will soon receive a response from us </h2>")    
        else:
            print(form.errors)
    context={
        "form":form
    }            
    return render(request,"repeat_course.html",context)

def scholarshipsF(request):
    obj=Scholarship.objects.all()
    context={
        "object":obj
    }
    return render(request,"scholarships.html",context)    

def scholarshipupload(request):
    form=scholarshipf()
    if request.method=="POST":
        form=scholarshipf(request.POST,request.FILES)
        if form.is_valid():
            Scholarship.objects.create(**form.cleaned_data)
            return  HttpResponse("<h1 align='center'> Scholarship page uploaded Successfully </h1>")
        else:
            print(form.errors)

    context={
        "form":form
    }            
    return render(request,"uploadscholarship.html",context)


def apply_scholarship(request):
    form=scholarship_dataf()
    if request.method=="POST":
        form=scholarship_dataf(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email_address']


            context={
                "form":name
            }
            my_subject="Scholarship application Verification"
            html_message=render_to_string('scholarship_email.html',context)
            plain_message=strip_tags(html_message)
            message=EmailMultiAlternatives(
                body=plain_message,
                from_email=None,
                subject=my_subject,
                to=[
                    email])
            message.attach_alternative(html_message,"text/html")
            try:
                message.send()
                Scholarship_data.objects.create(**form.cleaned_data)
                return HttpResponse("<h1 align='center'>Application Submitted successfully  <br>You will soon receive a message fro us </h1>")

            except:
                return HttpResponse("<h1 align='center'>There is some problem please try again</h1>")


        else:
            print(form.errors)
    context={
        "form":form
    }
    return render(request,"scholarship_apply_form.html",context)            

def admission(request):
    obj=Admission.objects.all()
    context={
        "object":obj
    }
    return render(request,"admission_data.html",context)    
def scholarship(request):
    obj=Scholarship_data.objects.all()
    context={
        "object":obj
    }
    return render(request,"scholarship_data.html",context)    
def admin(request):
    return render(request,"admin_option.html")       

def parking(request):
    obj=Car_parking.objects.all()
    context={
        "object":obj
    }
    return render(request,"car_parking_data.html",context)         

def feed(request):    
    obj=Fee.objects.all()
    context={
        "object":obj
    }
    return render(request,"fee_data.html",context)

def library_card(request):
    obj=Library.objects.all()
    context={
        "object":obj
    }    
    return render(request,'library_data.html',context)
def repeat(request):
    obj=Repeat_course.objects.all()
    context={
        "object":obj
    }
    return render(request,"repeat_data.html",context)    

def new(request):
    return render(request,'Quid.html')   

def get_detail(request):
    form=Detail()
    if request.method=="POST":
        form=Detail(request.POST)
        if form.is_valid:
            cnic=request.POST['cnic']
            query=f"select* from myapp_signup where cnic = '{cnic}' "
            cursor.execute(query)
            variable=cursor.fetchone()
            if variable is not None:
                context1={
                    "name":variable[0],
                    "father_name":variable[1],
                    "phone_number":variable[2],
                    "email":variable[3],
                    "password":variable[4],
                    "cnic":variable[5]
                }
                html_message=render_to_string('detail_email.html',context1)
                plain_message=strip_tags(html_message)
                my_subject="Data Recovery email "
                message=EmailMultiAlternatives(
                    body=plain_message,
                    subject=my_subject,
                    to=[variable[3]],
                    from_email=None
                )
                message.attach_alternative(html_message,"text/html")
                message.send()
                messages.success(request,"An email has been sent to the email related to this cnic ")
    context2={
        "form":form
    }            
    return render(request,"request_for_detail.html",context2)    



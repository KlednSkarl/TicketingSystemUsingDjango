from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.hashers import make_password 
from .models import (Tbl_AdmUser,TblAdmDepartment,userCredentials)
import uuid

# Create your views here.

import uuid
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import Tbl_AdmUser, TblAdmDepartment, userCredentials


@transaction.atomic
def user_Adding(request):
    if request.method != "POST":
        return redirect("userAdding")

    try:
        if userCredentials.objects.filter(
            LI_userName=request.POST.get("username")
        ).exists():
            messages.error(request, "Username already exists")
            return redirect("userAdding")

        credentials = userCredentials.objects.create(
            LI_userID=str(uuid.uuid4()),
            LI_userName=request.POST.get("username"),
            LI_passWord=make_password(request.POST.get("password"))
        )

        Tbl_AdmUser.objects.create(
            credentials=credentials,
            fname=request.POST.get('fname'),
            mname=request.POST.get('mname'),
            lname=request.POST.get('lname'),
            bday=request.POST.get('bday'),
            sex=request.POST.get('sex'),
            contactNo=request.POST.get('contactNo'),
            address=request.POST.get('address'),

            isAdmin='isAdmin' in request.POST,
            isUser='isUser' in request.POST,
            isDeploy='isDeploy' in request.POST,

            dept_id=request.POST.get('dept') or None
        )

        messages.success(request, "User successfully created")
        return redirect("userAdding")

    except Exception as e:
        messages.error(request, f"Error creating user: {e}")
        return redirect("userAdding")









def Landing_Page(request):
    return render(request,'UI_LandingPage.html')
#this renders the landing page on the empty link

def DashBoard(request):
    return render(request,'UI_Dashboard.html')
# renders dashboard for MIS program 

def UI_userLogin(request): 
    error =None
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=userCredentials.objects.get(
                LI_userName = username,
                LI_passWord = password    
                )
            request.session['LI_userID'] = user.LI_userID
            request.session['LI_userName'] = user.LI_userName
            return redirect('DashBoard')
        
        except  userCredentials.DoesNotExist:
            error = "Invalid username and password"
    return render(request,'UI_userLogIn.html',{'error': error})
    # query that checks the username and password, 
    # while also throwing a value back to the html if there is an error
    # this also renders the UI for userlogin

def logout_view(request):
        request.session.flush()
        return redirect('Landing_Page')
# render landing page after session logout


def UI_userMaintenance(request):
     return render(request,'UI_UserMaintenance.html')
# render maintenance UI

def UI_UserAdding(request):
     return render(request,'UI_UserAdding.html')
# render User adding
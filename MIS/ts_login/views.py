from django.shortcuts import render,redirect
from userLogin.models import userCredentials
from userLogin.models import Tbl_AdmUser


def UI_TicketSystem_Login(request):
    error =None
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user=userCredentials.objects.get(
                LI_userName = username,
                LI_passWord = password )

            adm_user = Tbl_AdmUser.objects.filter(credentials = user).first()   

            if not adm_user:
                error = "User profile not set up"
                return render(request,'UI_TicketSystem_Login.html',{'error':error})


            request.session['LI_userID'] = user.LI_userID
            request.session['LI_userName'] = user.LI_userName


            # Imported admin access
            request.session['isAdmin'] = adm_user.isAdmin
            request.session['isUser'] = adm_user.isUser
            request.session['isDeploy'] = adm_user.isDeploy
         




            return redirect('UI_TicketSystem_Dashboard')
        
        except userCredentials.DoesNotExist:
            error = "Invalid username and password"
    return render(request,'UI_TicketSystem_Login.html',{'error': error})

def UI_TicketSystem_Dashboard(request):
    return render(request,'UI_TicketSystem_Dashboard.html')


 

 


# Create your views here.

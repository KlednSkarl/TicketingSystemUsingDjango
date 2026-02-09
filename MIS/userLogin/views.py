from django.shortcuts import render, redirect,get_object_or_404
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.hashers import make_password 
from .models import (Tbl_AdmUser,TblAdmDepartment,userCredentials)
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password
from django.db.models.deletion import ProtectedError
import uuid

# Create your views here.
  

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
        #adding users





def Landing_Page(request):
    return render(request,'UI_LandingPage.html')
#this renders the landing page on the empty link






def DashBoard(request):
    user_count = Tbl_AdmUser.objects.count()
    return render(request,'UI_Dashboard.html',{'user_count':user_count})
# renders dashboard for MIS program while passing count of users in the table 








def UI_userLogin(request): 
    error =None
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=userCredentials.objects.get(
                LI_userName = username    
                )
            if check_password(password,user.LI_passWord):
                request.session['LI_userID'] = user.LI_userID
                request.session['LI_userName'] = user.LI_userName
                return redirect('DashBoard')
            else:
                error = "Invalid password"  
        
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

        tblUsers = Tbl_AdmUser.objects.values('id',
        'fname','mname','lname','bday', 'sex','address', 'contactNo','isAdmin','isDeploy','isUser','dept'
    ).order_by('id')
        paginator = Paginator(tblUsers,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
     
     
        return render(request,
                      'UI_UserMaintenance.html',{'tblUsers': page_obj,
                                                 'page_obj' : page_obj})
# render maintenance UI







def deleteUser(request,id):
    delete_user = Tbl_AdmUser.objects.get(id=id)
    delete_user.delete()
    return redirect("/UserMaintenance")
# render user maintenance after deleting id



def UI_UserAdding(request):
    dept_Compilation = TblAdmDepartment.objects.all()
    return render(request,'UI_UserAdding.html',{'dept_Compilation' : dept_Compilation})
# render User adding




def UI_selectUsertUpdate(request, id):
    user = get_object_or_404(Tbl_AdmUser, id=id)
    userDept = TblAdmDepartment.objects.all()

    return render(request,'userLogin/UI_UpdateUserLogin.html', {
        'user': user,
        'userDept': userDept
    })

# select the ID before going through the process of querying the update

@transaction.atomic
def updateUserData(request,id):
    user= get_object_or_404(Tbl_AdmUser,id=id)
    userDept = TblAdmDepartment.objects.all()
    if request.method == "POST":
        try:
            user.fname = request.POST.get('fname')
            user.mname = request.POST.get('mname')
            user.lname = request.POST.get('lname')
            user.bday = request.POST.get('bday')
            user.sex = request.POST.get('sex')
            user.contactNo = request.POST.get('contactNo')
            user.address = request.POST.get('address')



            user.isAdmin = 'isAdmin' in request.POST
            user.isDeploy = 'isDeploy' in request.POST
            user.isUser =  'isUser' in request.POST
            user.dept_id = request.POST.get('dept') or None


            user.save()

            messages.success(request,"User Updated Successfully")
            return redirect('userMaintenance')
 
        except Exception as e:
            messages.error(request,f"Error {e}")
            return redirect('selectUsertUpdate',id=id)
        
    # updating user credentials  using ID 
    
@transaction.atomic
def updateDeptData(request,id):
    deptID = get_object_or_404(TblAdmDepartment,id=id)
 

    if request.method == "POST":
        try:
            deptID.dept=request.POST.get('ET_updateSelectedDepartment')

            deptID.save()

            messages.success(request,"Updating Complete")
            return redirect('deptMaintenance')

        except Exception as e:
            messages.error(request,"Unable to update department Error")
            return redirect("deptMaintenance",id=id)












def deptMaintenance(request):
        
        # ======for pagination =======
        dept_List = TblAdmDepartment.objects.all().order_by('id')
        paginator = Paginator(dept_List,5)
        page_number = request.GET.get('page')
        # ======== end of pagination variable ======


        dept_count = paginator.get_page(page_number)
        return render(request,'UI_DeptMaintenance.html',{'dept_count':dept_count})
    # render the UI for html

 









@transaction.atomic
def deptAdd(request):
    if request.method !="POST":
        return redirect("deptMaintenance")
        
    try:
        if TblAdmDepartment.objects.filter(
            dept = request.POST.get("ET_deptToAdd")).exists():    
            messages.error(request,"Department Already exists")
            return redirect("deptMaintenance")
             
        TblAdmDepartment.objects.create(
        dept =request.POST.get('ET_deptToAdd'))
        messages.success(request, "Department Added Successfully")
        return redirect("deptMaintenance")




    except Exception as e:
        messages.error(request,"Department Failed to Add")
        return redirect("deptMaintenance")  
    # adding department using modal



def deptDelete(request,id):
        delete_Dept= TblAdmDepartment.objects.get(id=id)
        

        try:
            delete_Dept.delete()
            messages.success(request,"Department Successfully Deleted") 
        except ProtectedError:
            messages.error(request,"Department has users inside")             
        return redirect('/deptMaintenance')
        # delete Department
 

 

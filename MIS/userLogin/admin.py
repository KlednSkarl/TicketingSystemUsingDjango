from django.contrib import admin
from .models import userCredentials
from .models import Tbl_AdmUser
from .models import TblAdmDepartment
# Register your models here.


@admin.register(userCredentials)
class UserCredentialAdmin(admin.ModelAdmin):
    list_display = ('LI_userID','LI_userName')


@admin.register(Tbl_AdmUser)
class Tbl_AdmUserAdmin(admin.ModelAdmin):
    list_display= ('fname','lname')

@admin.register(TblAdmDepartment)
class Tbl_TblAdmDepartment(admin.ModelAdmin):
    list_display = ('id','dept')
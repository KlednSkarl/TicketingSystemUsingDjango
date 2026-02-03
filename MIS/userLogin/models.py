from django.db import models
#from userLogin import models

# Create your models here.

class userCredentials(models.Model):
    LI_userID = models.CharField(max_length=100)
    LI_userName = models.CharField(max_length=100)
    LI_passWord = models.CharField(max_length=100)

    def __str__(self):
        return self.LI_userName


# for user logins
class TblAdmDepartment(models.Model):
    dept = models.CharField(max_length=100)
    def __str__(self):
        return self.dept
# for user tbl departments




class Tbl_AdmUser(models.Model):
    credentials = models.OneToOneField( userCredentials,on_delete=models.PROTECT,null=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    bday = models.DateField()

    sex= models.CharField( max_length=1, choices=[ ('M','Male'), ('F','Female')])

    address = models.TextField()
    contactNo = models.CharField(max_length=20)

    isAdmin = models.BooleanField(default=False)
    isUser = models.BooleanField(default = True)
    isDeploy = models.BooleanField(default = False)

    dept = models.ForeignKey(TblAdmDepartment, on_delete=models.PROTECT, null= True, blank =True)
#for users lezgo
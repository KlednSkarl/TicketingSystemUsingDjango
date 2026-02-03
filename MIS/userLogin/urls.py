from django.urls import path
from .views import UI_userLogin
from .views import Landing_Page
from .views import DashBoard
from .views import logout_view
from .views import UI_userMaintenance
from .views import UI_UserAdding
from .views import user_Adding
from .views import deleteUser
from .views import UI_selectUsertUpdate
from .views import updateUserData
from .views import deptMaintenance
from .views import deptDelete
from .views import deptAdd
from .views import updateDeptData





urlpatterns = [
    path('/userLogin',UI_userLogin,name='UI_userLogin'),
    path('',Landing_Page,name='Landing_Page'),
    path('dashboard/',DashBoard,name='DashBoard'),
    path('logout',logout_view,name ='logout'),
    path('UserMaintenance',UI_userMaintenance,name ='userMaintenance'),
    path('userAdding',UI_UserAdding,name = 'userAdding'),
    path('adduser',user_Adding, name = 'adduser'),
    path('deleteuser/<int:id>/',deleteUser, name ='deleteuser'),
    path('selectedUser/<int:id>/',UI_selectUsertUpdate, name ='selectedUser'),
    path('selectedUser/updateUserData/<int:id>/',updateUserData, name ='updateUserData'),
    path('deptMaintenance',deptMaintenance,name="deptMaintenance"),
    path('deptDelete/<int:id>',deptDelete,name='deptDelete'),
    path('deptAdd',deptAdd,name ="deptAdd"),
    path('updateDeptData/update/<int:id>/',updateDeptData,name ='updateDeptData'),
]
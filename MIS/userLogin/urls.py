from django.urls import path
from .views import UI_userLogin
from .views import Landing_Page
from .views import DashBoard
from .views import logout_view
from .views import UI_userMaintenance
from .views import UI_UserAdding
from .views import user_Adding

urlpatterns = [
    path('/userLogin',UI_userLogin,name='UI_userLogin'),
    path('',Landing_Page,name='Landing_Page'),
    path('dashboard/',DashBoard,name='DashBoard'),
    path('logout',logout_view,name ='logout'),
    path('UserMaintenance',UI_userMaintenance,name ='userMaintenance'),
    path('userAdding',UI_UserAdding,name = 'userAdding'),
    path('adduser',user_Adding, name = 'adduser')
]
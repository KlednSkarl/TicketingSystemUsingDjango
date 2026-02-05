from django.urls import path
from .views import UI_TicketSystem_Login
from .views import UI_TicketSystem_Dashboard

urlpatterns= [
     path('ui_TicketSystem_Login/',UI_TicketSystem_Login,name='ui_TicketSystem_Login'),
     path('ui_TicketSystem_Dashboard',UI_TicketSystem_Dashboard,name='UI_TicketSystem_Dashboard'),
     
     

]
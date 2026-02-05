from django.urls import path
from .views import UI_TicketSystem_Login
from .views import UI_TicketSystem_Dashboard
from .views import UI_showAllTicketCards
from .views import create_ticket
urlpatterns= [
     path('ui_TicketSystem_Login/',UI_TicketSystem_Login,name='ui_TicketSystem_Login'),
     path('ui_TicketSystem_Dashboard',UI_TicketSystem_Dashboard,name='UI_TicketSystem_Dashboard'),
     path('UI_ticketCompilation',UI_showAllTicketCards,name='UI_showAllTicketCards'),
     path('create_ticket',create_ticket,name ='create_ticket')

]
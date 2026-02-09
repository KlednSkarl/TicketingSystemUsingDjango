from django.urls import path
from .views import UI_TicketSystem_Login
from .views import UI_TicketSystem_Dashboard
from .views import UI_showAllTicketCards
from .views import create_ticket
from .views import UI_ticket_Management
from .views import update_ticket
urlpatterns= [
     path('ui_TicketSystem_Login/',UI_TicketSystem_Login,name='ui_TicketSystem_Login'),
     path('ui_TicketSystem_Dashboard',UI_TicketSystem_Dashboard,name='UI_TicketSystem_Dashboard'),
     path('UI_ticketCompilation',UI_showAllTicketCards,name='UI_showAllTicketCards'),
     path('create_ticket',create_ticket,name ='create_ticket'),
     path('UI_ticketManagement',UI_ticket_Management,name='UI_ticket_Management'),
     path('update_ticket',update_ticket, name='update_ticket')
]
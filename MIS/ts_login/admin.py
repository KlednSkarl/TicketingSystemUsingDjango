from django.contrib import admin
from ts_login.models import Ticket 
from userLogin.models import Tbl_AdmUser



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display= ('ticketCode','ticketSeverity')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ticketAuthor":
            kwargs["queryset"] = Tbl_AdmUser.objects.filter(isUser=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ticketAssignedTo":
            kwargs["queryset"] = Tbl_AdmUser.objects.filter(isDeploy=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ticketDeployer":
            kwargs["queryset"] = Tbl_AdmUser.objects.filter(isAdmin=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
    
# Register your models here.

 

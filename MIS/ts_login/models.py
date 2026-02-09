from django.db import models
from userLogin.models import Tbl_AdmUser
from django.db.models import Max




class Ticket(models.Model):

    ticketCode = models.CharField(max_length=200,unique=True)
    ticketSeverity = models.CharField(
        max_length=20,
        choices=[('LOW','Low'),
                 ('MEDIUM','Medium'),
                 ('HIGH','High'),
                 ('CRITICAL','Critical'),
                 ('DANGER','Danger')],
        default='LOW')
    


    ticketTitle = models.CharField(max_length=200)




    ticketBody = models.TextField()



    ticketAuthor = models.ForeignKey(
        Tbl_AdmUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="tickets_created"
    )



    ticketAssignedTo = models.ForeignKey(
        Tbl_AdmUser,
        on_delete=models.SET_NULL,
        null=True,
        blank = True,
        related_name="assigned_tickets"
    )
    ticketDeployer= models.ForeignKey(
        Tbl_AdmUser,
        on_delete=models.SET_NULL,
        null=True,
        blank = True,
        related_name="tickets_Deployed"
    )
    ticketStatus=models.CharField(
        max_length=50,
        choices=[('OPEN','Open'),('IN_PROGRESS','In Progress'),('RESOLVED','Resolved'),
                 ('CLOSED','Closed'),('REJECTED','Rejected')],default='OPEN'
    )
    ticketCreatedAt = models.DateTimeField(auto_now_add=True)
    ticketUpdatedAt = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def generateNewTicketCode():
        prefix= "TCK-IT"
        last_ticket = Ticket.objects.filter(
        ticketCode__startswith=prefix
        ).aggregate(
        max_code=Max('ticketCode')
        )['max_code']


        if last_ticket:
            last_number=int(last_ticket.replace(prefix,""))
            new_number = last_number +1
        else:
            new_number = 1
        return f"{prefix}{new_number:06d}"

    def save(self,*args,**kwargs):
        if not self.ticketCode:
            self.ticketCode = Ticket.generateNewTicketCode()
        super().save(*args,**kwargs)

    def status_class(self):
        return {
        'OPEN': 'table-primary',
        'IN_PROGRESS': 'table-warning',
        'RESOLVED': 'table-success',
        'CLOSED': 'table-secondary',
        'REJECTED': 'table-danger',
    }.get(self.ticketStatus, '')

# Create your models here.

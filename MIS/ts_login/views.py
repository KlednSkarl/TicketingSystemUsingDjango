from django.shortcuts import render,redirect,get_object_or_404
from userLogin.models import userCredentials
from userLogin.models import Tbl_AdmUser
from ts_login.models import Ticket
from django.core.paginator import Paginator
from .forms import TicketForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password



def UI_TicketSystem_Login(request):
    error =None
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user=userCredentials.objects.get(
                LI_userName = username)
            if check_password(password,user.LI_passWord):
                adm_user = Tbl_AdmUser.objects.filter(credentials = user).first()   

            if not adm_user:
                error = "User profile not set up"
                return render(request,'UI_TicketSystem_Login.html',{'error':error})


            request.session['LI_userID'] = user.LI_userID
            request.session['LI_userName'] = user.LI_userName


            # Imported admin access
            request.session['isAdmin'] = adm_user.isAdmin
            request.session['isUser'] = adm_user.isUser
            request.session['isDeploy'] = adm_user.isDeploy
         




            return redirect('UI_TicketSystem_Dashboard')
        
        except userCredentials.DoesNotExist:
            error = "Invalid username and password"
    return render(request,'UI_TicketSystem_Login.html',{'error': error})

def UI_TicketSystem_Dashboard(request):
    return render(request,'UI_TicketSystem_Dashboard.html')


def UI_showAllTicketCards(request):
    ticketTable_count = Ticket.objects.all().order_by('id')
    paginator= Paginator(ticketTable_count,5)
    page_number = request.GET.get('page')


    ticketTable = paginator.get_page(page_number)

    return render(request,'UI_ticketCompilation.html',{'ticketTable':ticketTable})



 
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)

            try:
                credentials = get_object_or_404(
                    userCredentials,
                    LI_userName=request.user.username
                )
            except userCredentials.DoesNotExist:
                raise Exception("No userCredentials for this Django user")

            try:
                adm_user = Tbl_AdmUser.objects.get(credentials=credentials)
            except Tbl_AdmUser.DoesNotExist:
                raise Exception("No Tbl_AdmUser linked to credentials")

            ticket.ticketAuthor = adm_user
            ticket.save()

            return redirect('create_ticket')
    else:
        form = TicketForm()

    return render(request, 'UI_CreateTicket.html', {'form': form})



def UI_ticket_Management(request):
    logged_user = None
    is_admin = False

    if request.user.is_authenticated:
        try:
            credentials = userCredentials.objects.get(
                LI_userName=request.user.username
            )
            logged_user = Tbl_AdmUser.objects.get(credentials=credentials)
            is_admin = logged_user.isAdmin
        except (userCredentials.DoesNotExist, Tbl_AdmUser.DoesNotExist):
            pass

    ticket_qs = Ticket.objects.all().order_by('-ticketCreatedAt')
    paginator = Paginator(ticket_qs, 5)
    page_number = request.GET.get('page')
    ticketTable = paginator.get_page(page_number)


    forDeploy = Tbl_AdmUser.objects.filter(isDeploy=True)
    forAdmin = Tbl_AdmUser.objects.filter(isAdmin=True)
     

    return render(
        request,
        'UI_ticketManagement.html',
        {
            'ticketTable': ticketTable,
            'is_admin': is_admin,
            'forDeploy': forDeploy,
            'forAdmin': forAdmin,
            'status_choices': Ticket._meta.get_field('ticketStatus').choices,
        }
    )

def update_ticket(request):
    if request.method != "POST":
        return redirect("UI_ticket_Management")

    ticket_id = request.POST.get("ticket_id")
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Update status
    ticket_status = request.POST.get("ticket_status")
    if ticket_status in dict(Ticket._meta.get_field("ticketStatus").choices):
        ticket.ticketStatus = ticket_status

    # Update assigned employee
    assigned_to = request.POST.get("assigned_to")
    if assigned_to:
        ticket.ticketAssignedTo_id = assigned_to
    else:
        ticket.ticketAssignedTo = None

    # Update deployer
    deployed_by = request.POST.get("deployed_by")
    if deployed_by:
        ticket.ticketDeployer_id = deployed_by
    else:
        ticket.ticketDeployer = None

    ticket.save(update_fields=[
        "ticketStatus",
        "ticketAssignedTo",
        "ticketDeployer",
        "ticketUpdatedAt"
    ])

    messages.success(request, "Ticket updated successfully")
    return redirect("UI_ticket_Management")




# Renders the UI for ticket management while also passing 
# the is_admin boolean value for access verification
















# Create your views here.

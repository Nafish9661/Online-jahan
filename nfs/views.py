from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as sfk
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .Middleware import auth, guest
import requests
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


from .models import Admit_Card,WhatsAppMessage, Enquiry, Result, Addmision,CustomUser,Partner_Registration, Govt_Scheme, Latest_job, incentive, Application, Multi_Post
# Create your views here.
User = get_user_model()


def index(request):
    sidh = Admit_Card.objects.all().order_by("-id")[0:15]
    khal = Govt_Scheme.objects.all().order_by("-id")[0:15]
    job= Latest_job.objects.all().order_by("-id")[0:15]
    Add= Addmision.objects.all().order_by('-id')[0:15]

    cc = {'sidh' : sidh, 'khal': khal, 'job' : job, 'Add': Add}
    
    return render(request, "index.html", cc)


def L_job(request, slug):
    TEMPLATE_NAME = 'application'
    incen = Latest_job.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
    a = '/job/'
    b = incen.slug
    link =  a + b
    Amount = int(incen.ServiceCharge) + int(incen.Payment)
    Docs = incen.SupportingDoc
    Payment_link = incen.Payment_Link+str(100)
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        State = request.POST.get('State')
        
        if Application.objects.filter(Mobile=Mobile, Target_Url=link).exists():
            messages.warning(request, 'Mobile No is already exist!!')
            PP= (link)

            return redirect(PP)
        
        App = Application(Applicant_Name=Name, Mobile=Mobile, State=State, Form_Type='Latest Job',Target_Url=(link))
        App.save()
        messages.success(request, 'Your Request Submitted Successfully')
        response = send_whatsapp_message(Mobile, Name,Docs, Amount, Payment_link, TEMPLATE_NAME)
        print(response)  # Log the response or handle errors if needed
    return render(request, 'incentive.html', ins)


def GovtScheme(request, slug):
    TEMPLATE_NAME = 'application'
    incen = Govt_Scheme.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
    a = '/govtscheme/'
    b = incen.slug
    link = a+b
    Amount = incen.ServiceCharge
    Docs = incen.SupportingDoc
    Payment_link = incen.Payment_Link + incen.ServiceCharge

    
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        State = request.POST.get('State')
        
        
        if Application.objects.filter(Mobile=Mobile, Target_Url=link).exists():
            messages.warning(request, 'Mobile No is already exist!!')
            return redirect (link)
        App = Application(Applicant_Name=Name, Mobile=Mobile, State=State, Form_Type="Govt Scheme",Target_Url=link)
        App.save()
        messages.success(request, 'Your Request Submitted Successfully')
        response = send_whatsapp_message(Mobile, Name,Docs, Amount,Payment_link, TEMPLATE_NAME)
        print(response)  # Log the response or handle errors if needed
    return render(request, 'incentive.html', ins)

def Results(request):
    data = Result.objects.all().order_by('-id')
    data = {'data' : data}
    return render(request, 'result.html', data)


def admit(request, slug):
    incen = Addmision.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
    a = '/admit/'
    b = incen.slug
    link= a+b
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        State = request.POST.get('State')
        District= request.POST.get('District')
        
        if Application.objects.filter(Mobile=Mobile, Target_Url=link).exists():
            messages.warning(request, 'Mobile No is already exist!!')
            return redirect (link)
        App = Application(Applicant_Name=Name, District=District, Mobile=Mobile, State=State, Form_Type='Addmission',Target_Url=link)
        App.save()
    return render(request, 'incentive.html', ins)

# def enquiry(request):
    
#     if request.method == 'POST':
#         Name = request.POST.get('name')
#         Email = request.POST.get('email')
#         Message = request.POST.get('message')
        
#         if Enquiry.objects.filter(Email_nfs=Email).exists():
#             messages.warning(request, 'Email is already exist!!')
#             return render (request, 'enquiry.html')
#         enquiry = Enquiry(Name_nfs=Name, Email_nfs=Email, Message_nfs=Message)
#         enquiry.save()
#         messages.success(request, 'Your Message Submitted Successfully!')

#     return render(request, 'enquiry.html')

# def Partner(request):
    
#     if request.method == 'POST':
#         Name = request.POST.get('Name')
#         Father = request.POST.get('Father')
#         State = request.POST.get('State')
#         District = request.POST.get('District')
#         Address = request.POST.get('Address')
#         Mobile = request.POST.get('Mobile')
#         Email = request.POST.get('Email')
#         Remark = request.POST.get('Remark')
        
#         if Partner_Registration.objects.filter(Email=Email).exists():
#             messages.warning(request, 'Email is already exist!!')
#             return render (request, 'partner_form.html')
#         partner = Partner_Registration(Name=Name, Father=Father, State=State,District=District,Address=Address,Mobile=Mobile,Remark=Remark)
#         partner.save()
#         messages.success(request, 'Your Registration Form Submitted Successfully!')

#     return render(request, 'partner_form.html')

def AdmitCard(request, slug):
    incen = Admit_Card.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
  
    return render(request, 'print.html', ins)

def ResultPrint(request, slug):
    incen = Result.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
  
    return render(request, 'print.html', ins)

# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render


# This is only for test

from django.http import JsonResponse


@guest
def Login(request):
    if request.method=='POST':
        email =request.POST.get('email')
        password=request.POST.get('password')
        if email and password:

            user=authenticate(email=email,password=password)
            if user is not None:
                sfk(request, user)
                return redirect('dashboard')
            
            else:
                return HttpResponse('Please enter valid credential')
    return render (request, 'admin.html')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully logged Out')
    return redirect('nfs')


def user(request):
    Data = Application.objects.all()


@guest
def SignUp(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check if email is already in use
        if user.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return render(request, 'signup.html')

        # Create user
        user = user.objects.create_user(username=email, mobile=mobile, password=password1, first_name=name)
        user.save()

        return redirect('login')  # Redirect to a success page

    return render(request, 'signup.html')



@auth
def dashboard(request):
    user = request.user
    
    if user.is_superuser:
        applications = Application.objects.filter(Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Payment_Recieved=True,Initiated=True, Completed=False ).order_by("-id")
        comp= Application.objects.filter(Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    else:
        user_district = user.Assign_To
        applications = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=True, Completed=True )
        comp= Application.objects.filter(Assign_To=user_district,Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    application_count = applications.count()
    process_count = process.count()
    completed_count = comp.count()
    
    context = {
        'user': user,
        'applications': applications,
        'application_count': application_count,
        'process_count' : process_count,
        'completed_count' : completed_count

    }
    
    return render(request, 'test.html', context)
@auth
def userdata(request,application_id):
    user = request.user

    if user.is_superuser:
        applications = Application.objects.filter(Payment_Recieved=True).order_by("-id")
    else:
        user_district = user.Assign_To
        applications = Application.objects.filter(District=user_district, Payment_Recieved=True).order_by("-id")
    application = get_object_or_404(applications, id=application_id)
    if request.method == 'POST':
        is_application_initiated = request.POST.get('question1') == 'yes'
        is_form_completed = request.POST.get('question2') == 'yes'
        remarks = request.POST.get('remarks', '')
        
        application.Initiated = is_application_initiated
        application.Completed = is_form_completed
        application.Remarks = remarks
        application.save()
        messages.success(request, 'Status Updated Successfully')
        return redirect('userdata', application_id=application.id)
        
    return render(request, 'userdetails.html', {'application' : application})
    
@auth
def Process_Application(request):
    user = request.user
    
    if user.is_superuser:
        applications = Application.objects.filter(Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Payment_Recieved=True,Initiated=True, Completed=False).order_by("-id")
        comp= Application.objects.filter(Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    else:
        user_district = user.Assign_To
        applications = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=True, Completed=False ).order_by("-id")
        comp= Application.objects.filter(Assign_To=user_district,Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    process_count = process.count()
    application_count = applications.count()
    completed_count= comp.count()
    
    context = {
        'user': user,
        'process': process,
        'process_count': process_count,
        'application_count' : application_count,
        'completed_count' : completed_count

    }
    
    return render(request, 'In_Process.html', context)

@auth
def Compelete_Application(request):
    user = request.user
    
    if user.is_superuser:
        applications = Application.objects.filter(Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Payment_Recieved=True,Initiated=True, Completed=False ).order_by("-id")
        compeleted= Application.objects.filter(Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    else:
        user_district = user.Assign_To
        applications = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=False ).order_by("-id")
        process = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True,Initiated=True, Completed=False ).order_by("-id")
        compeleted= Application.objects.filter(Assign_To=user_district,Payment_Recieved=True,Initiated=True,Completed=True ).order_by("-id")

    process_count = process.count()
    application_count = applications.count()
    compeleted_count = compeleted.count()
    
    context = {
        'user': user,
        'compeleted': compeleted,
        'process_count': process_count,
        'application_count' : application_count,
        'compeleted_count' : compeleted_count
    }
    
    return render(request, 'completed.html', context)



@auth
def All_Applications(request):

    user = request.user

    if user.is_superuser:
        applications = Application.objects.filter(Payment_Recieved=True).order_by("-id")
    else:
        user_district = user.Assign_To
        applications = Application.objects.filter(Assign_To=user_district, Payment_Recieved=True).order_by("-id")
    
    context = {
        'user': user,
            'applications': applications,}

    return render(request , 'all.html', context)
            
def check_status(request):
    status = None
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        try:
            application = Application.objects.get(Mobile=mobile)
            status = [application]
        except Application.DoesNotExist:
            status = 'Application not found.'
        except Application.MultipleObjectsReturned:
            applications = Application.objects.filter(Mobile=mobile)
            status = applications
    return render(request, 'status.html', {'status': status})



def Br_More(request):
    data = Govt_Scheme.objects.all().order_by('-id')
    data = {'data' : data}
    return render(request, 'Br_More.html', data)


def Cent_More(request):
    data = Admit_Card.objects.all().order_by('-id')
    data = {'data' : data}
    return render(request, 'Cent_More.html', data)


def Latest_Job_More(request):
    data = Latest_job.objects.all().order_by('-id')
    data = {'data' : data}
    return render(request, 'Latest_job_More.html', data)

def Admit_More(request):
    data = Addmision.objects.all().order_by('-id')
    data = {'data' : data}
    return render(request, 'Admit_More.html', data)

def Rtps(request):
    data = Multi_Post.objects.filter(Category='RTPS')
    return render(request, 'Multi.html', {'data': data})

def Mutation(request):
    data = Multi_Post.objects.filter(Category='Mutation/Lagaan')
    return render(request, 'Multi.html', {'data': data})

def Scholarship(request):
    data = Multi_Post.objects.filter(Category='Scholarship')
    return render(request, 'Multi.html', {'data': data})

def Anudan(request):
    data = Multi_Post.objects.filter(Category='Anudan')
    return render(request, 'Multi.html', {'data': data})

def Passport(request):
    data = Multi_Post.objects.filter(Category='Pan Card')
    return render(request, 'Multi.html', {'data': data})

def Farmer(request):
    data = Multi_Post.objects.filter(Category='Farmer')
    return render(request, 'Multi.html', {'data': data})


def Rtps_View(request, slug):
    TEMPLATE_NAME = 'testing'
    incen = Multi_Post.objects.filter(slug=slug).first()
    ins = {'incen' : incen}
    a = '/Multi/'
    b = incen.slug
    link =  a + b
    if request.method == 'POST':
        Name = request.POST.get('name')
        Mobile = request.POST.get('mobile')
        State = request.POST.get('State')
        District= request.POST.get('District')
        if Application.objects.filter(Mobile=Mobile, Target_Url=link).exists():
            messages.warning(request, 'Mobile No is already exist!!')
            PP= (link)

            return redirect(PP)
        App = Application(Applicant_Name=Name,District=District, Mobile=Mobile, State=State, Form_Type=incen.Category,Target_Url=(link))
        App.save()
        messages.success(request, 'Your Request Submitted Successfully')
        response = send_whatsapp_message(Mobile, Name, TEMPLATE_NAME)
        print(response)  # Log the response or handle errors if needed
    return render(request, 'Multi_Post.html', ins)

@auth
def search_applications(request):
    user = request.user


    query = request.GET.get('q')
    if user.is_superuser:
        results = Application.objects.filter(Payment_Recieved=True)
    else:
        user_district = user.Assign_To
        results = Application.objects.filter(Assign_To=user_district,Payment_Recieved=True)

    if query:
        
        results = results.filter(Mobile__icontains=query, ) | results.filter(Applicant_Name__icontains=query)
        
        context = {
            'results': results,
            'query': query,
        }

        return render(request, 'search.html', context)
    return render(request, 'search.html')




# from django.shortcuts import render
# from django.contrib import messages
# from .models import Enquiry
# from .whatsapp_service import WhatsAppAPI  # Import the WhatsAppAPI class

def enquiry(request):
    TEMPLATE_NAME = 'testing'
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Message = request.POST.get('message')

        if Enquiry.objects.filter(Email_nfs=Email).exists():
            messages.warning(request, 'Email is already exist!!')
            return render(request, 'enquiry.html')
        response = send_whatsapp_message(Phone, Name, TEMPLATE_NAME)
        print(response)
        # Save enquiry to the database
        enquiry = Enquiry(Name_nfs=Name, Email_nfs=Email, Message_nfs=Message)
        enquiry.save()
        messages.success(request, 'Your Message Submitted Successfully!')

        # # Send WhatsApp message
        # access_token = settings.ACCESS_TOKEN
        # phone_number_id = settings.PHONE_NUMBER_ID
        # template_name = 'nfs'
        # language_code = 'en'
        # to_number = ('91' + Phone)  # This should be the user's number or a default admin number

        # # Initialize the API service
        # whatsapp_api = WhatsAppAPI(access_token, phone_number_id)

        # # Send template message
        # response = whatsapp_api.send_template_message(to_number, template_name, language_code)

        # # Handle the response if needed
        # print(response)  # Or use logging instead

    return render(request, 'enquiry.html')



# WhatsApp API Configuration
ACCESS_TOKEN = settings.ACCESS_TOKEN
PHONE_NUMBER_ID = settings.PHONE_NUMBER_ID

def send_whatsapp_message(phone_number, name, Document, Amount, payment, TEMPLATE_NAME,):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    data = {
        "messaging_product": "whatsapp",
        "to": ('91' + phone_number),
        "type": "template",
        "template": {
            "name": TEMPLATE_NAME,
            "language": {"code": "en"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {"type": "text", "text": name}
                        
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": Document},
                        {"type": "text", "text": Amount}
                    ]
                },
                
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [
                        {"type": "text","text": payment} 
                        
                    ]
                },
                          
            ]
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def Partner(request):
    TEMPLATE_NAME = 'aplication'

    if request.method == 'POST':
        Name = request.POST.get('Name')
        Father = request.POST.get('Father')
        State = request.POST.get('State')
        District = request.POST.get('District')
        Address = request.POST.get('Address')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        Remark = request.POST.get('Remark')

        if Partner_Registration.objects.filter(Email=Email).exists():
            messages.warning(request, 'Email is already exist!!')
            return render(request, 'partner_form.html')

        partner = Partner_Registration(
            Name=Name, Father=Father, State=State, District=District,
            Address=Address, Mobile=Mobile, Remark=Remark
        )
        partner.save()
        messages.success(request, 'Your Registration Form Submitted Successfully!')

        # Send WhatsApp message
        response = send_whatsapp_message(Mobile, Name, TEMPLATE_NAME)
        print(response)  # Log the response or handle errors if needed

    return render(request, 'partner_form.html')


def whatsapp_webhook(request):
    if request.method == 'GET':
        # Webhook verification challenge
        verify_token = '9199376012'  # Your verify token
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if mode == 'subscribe' and token == verify_token:
            return HttpResponse(challenge)
        else:
            return HttpResponse(status=403)

    elif request.method == 'POST':
        # Process the incoming message from WhatsApp
        payload = json.loads(request.body.decode('utf-8'))
        entry = payload.get('entry', [])

        for item in entry:
            changes = item.get('changes', [])
            for change in changes:
                value = change.get('value', {})
                messages = value.get('messages', [])

                for message in messages:
                    from_number = message.get('from')
                    message_body = message.get('text', {}).get('body', '')

                    # Store the message in the database
                    WhatsAppMessage.objects.create(
                        from_number=from_number,
                        message_body=message_body
                    )

                    # Log or take further actions based on the message content
                    print(f"Received message from {from_number}: {message_body}")

        return JsonResponse({"status": "success"}, status=200)
    


def display_messages(request):
    messages = WhatsAppMessage.objects.all().order_by('-timestamp')
    return render(request, 'messages.html', {'messages': messages})



def payment(request):
    return render (request, 'Payment_Link.html')
from django.contrib import admin
from django.urls import path
from nfs import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='nfs'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('govtscheme/<slug>/', views.GovtScheme),
    path('admitcard/<slug>/', views.AdmitCard),
    path('job/<slug>/', views.L_job, name='aaa'),
    path('job/<slug>/', views.Application, name='application'),
    path('admit/<slug>/', views.admit),
    path('Login', views.Login, name='Login'),
    # path('SignUp', views.SignUp, name='SignUp'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('Process_Application', views.Process_Application, name='Process_Application'),
    path('All_Applications', views.All_Applications, name='All_Applications'),
    path('check_status', views.check_status, name='check_status'),
    path('govtshcemes', views.Br_More, name='govtshceme'),
    path('admitcard', views.Cent_More, name='admitcard'),
    path('admisions', views.Admit_More, name='Admit_More'),
    path('latestjobs', views.Latest_Job_More, name='Latest_Job_More'),
    path('Rtps', views.Rtps, name='Rtps'),
    path('Mutation', views.Mutation, name='Mutation'),
    path('Scholarship', views.Scholarship, name='Scholarship'),
    path('Anudan', views.Anudan, name='Anudan'),
    path('Passport', views.Passport, name='Passport'),
    path('Farmer', views.Farmer, name='Farmer'),
    path('Multi/<slug>/', views.Rtps_View, name='Rtps_View'),
    path('logout', views.handlelogout, name='logout'),
    path('Finalized', views.Compelete_Application, name='Complete'),
    path('search', views.search_applications, name='search'),
    path('partnerform', views.Partner, name='partner'),
    path('result', views.Results, name='Result'),

    path('result/<slug>/', views.ResultPrint, name='ResultPrint'),


    path('userdata/<int:application_id>/', views.userdata, name='userdata'),
    path('webhook/', views.whatsapp_webhook, name='whatsapp_webhook'),
    path('messages/', views.display_messages, name='display_messages'),
    path('payment', views.payment, name= 'payment_link')
   


]
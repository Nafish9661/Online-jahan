from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Enquiry,WhatsAppMessage, Result,Admit_Card,Addmision,Partner_Registration,CustomUser, Govt_Scheme, Latest_job, incentive, Application, Multi_Post
# Register your models here.
# admin.site.site.header= 'Nafish Communication'
# admin.site.site_title= 'Online Duniya'
# admin.sie.index_title= 'Welcome to Nafish Communication'

class List_Application(admin.ModelAdmin):
    list_display =('Applicant_Name', 'Mobile', 'District', 'clickable_url', 'Initiated','Completed', 'Created_At', 'upload')
    readonly_fields = ('Form_Type',)
    list_filter = ('Is_Done', 'Created_At', 'Form_Type')
    search_fields = ('Applicant_Name', 'Mobile', 'State')
    # Queryset (Mark, Unmark)
    model = Application
    fields= ['Applicant_Name', 'Mobile','Assign_To', 'District', 'Form_Type','Payment_Recieved' ,'Amount', 'Payment_Mode', 'Transaction_id', 'Remarks']
    actions = ['Mark_Done', 'Unmark_Done']
    list_display =('Applicant_Name', 'Mobile', 'District', 'clickable_url','Payment_Recieved','Initiated','Completed', 'Form_Type', 'Created_At')
    
    def Mark_Done(self, request, queryset):
        queryset.update(Is_Done=True)
    def Unmark_Done(self, request, queryset):
            queryset.update(Is_Done=False)








# admin.site.register(Custom_User)
admin.site.register(Enquiry)
admin.site.register(Admit_Card)
admin.site.register(Addmision)
admin.site.register(Govt_Scheme)
admin.site.register(Latest_job)
admin.site.register(incentive)
admin.site.register(Application, List_Application)
admin.site.register(Multi_Post)
admin.site.register(Partner_Registration)
admin.site.register(Result)
admin.site.register(WhatsAppMessage)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'Assign_To', 'State')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')})
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
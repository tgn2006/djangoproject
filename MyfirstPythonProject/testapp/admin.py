from django.contrib import admin
from testapp.models import Membership

# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'first_name' ,'last_name','phone_number', 'email_address', 'address'  ]

admin.site.register(Membership,MembershipAdmin)

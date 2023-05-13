from django.contrib import admin
from .models import * 
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_id','name','key')
    
admin.site.register(Company,CompanyAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display=('device_id','company_id','name','IP','port')
admin.site.register(Device,DeviceAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('device_id','name')
    
admin.site.register(Employee,EmployeeAdmin)

class NewEmployeeAdmin(admin.ModelAdmin):
     list_display=('device_id','name')
     
admin.site.register(NewEmployee,NewEmployeeAdmin)

class AttandanceAdmin(admin.ModelAdmin):
    list_display = ('Date','time')

admin.site.register(Attandance,AttandanceAdmin)
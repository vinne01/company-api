from django.contrib import admin
from api.models import Company,Employee

# Register your models here.
#
#customized admin panel for company api
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
#we used list_filter for filter according to parameter pass     
    list_filter=('name',)

#customized admin panel for employee api
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','phone') 
# search any things through search_fields     
    search_fields=('email',)   

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
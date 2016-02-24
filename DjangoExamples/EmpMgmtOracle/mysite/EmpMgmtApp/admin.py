from django.contrib import admin
from mysite.EmpMgmtApp.models import Emp,Dept,DemoCustomers,DemoOrderItems,DemoOrders,DemoProcudtInfo,DemoStates,DemoUsers
#from django.contrib.admin.templatetags.admin_list import date_hierarchy


#admin user id:sumkuma2_orcl ,pwd:oracledb
class EmpAdmin(admin.ModelAdmin):
    list_display = ('empno','ename','job','mgr','hiredate','sal')
    list_filter = ['hiredate']
    search_fields = ['ename']
    date_hierarchy = 'hiredate'


# Register your models here.
admin.site.register(Emp,EmpAdmin)
admin.site.register(Dept)
admin.site.register(DemoCustomers)
admin.site.register(DemoOrderItems)
admin.site.register(DemoOrders)
admin.site.register(DemoProcudtInfo)
admin.site.register(DemoStates)
admin.site.register(DemoUsers)

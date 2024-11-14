from django.contrib import admin
from .models import *

admin.site.site_header = " Research Management System "
admin.site.site_title = " Research Admin Portal"
admin.site.index_title = "Welcome to Research Management System Admin"
# Register your models here.
admin.site.register(Department)
admin.site.register(Organization)
admin.site.register(PrincipleInvestigator)
admin.site.register(EndorsementForm)
admin.site.register(Budget)
admin.site.register(RecievedAmount)
admin.site.register(Installment)
admin.site.register(FinancialYear)
admin.site.register(Expenditure)

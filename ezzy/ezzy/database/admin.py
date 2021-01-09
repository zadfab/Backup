from django.contrib import admin
from .models import customer_table,message_forwarding_log,scheduler_table,template_table
# Register your models here.
admin.site.register(customer_table)
admin.site.register(message_forwarding_log)
admin.site.register(scheduler_table)
admin.site.register(template_table)
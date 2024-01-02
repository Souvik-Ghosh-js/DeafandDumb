from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Query , Guardian ,Student ,AdmissionData

# Register your models here.
admin.site.register(Query)
admin.site.register(Guardian)
admin.site.register(Student)
admin.site.register(AdmissionData)

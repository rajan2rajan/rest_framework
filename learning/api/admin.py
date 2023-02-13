from django.contrib import admin
from .models import Database


# Register your models here.

@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ['id','firstname',"middlename" ,"lastname" , "age" , "contactnumber" , "incident" , "bloodgroup" , "Gender" , "location" ,  "unit" ,  "emergency" , "requiredate"] 
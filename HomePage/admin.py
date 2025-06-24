from django.contrib import admin
from .models import User_Data_all


class User_Data_allAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'created_on')
    search_fields = ('First_Name', 'Last_Name', 'Nid_card_number')
    list_filter = ('created_on',)

    
admin.site.register(User_Data_all,User_Data_allAdmin)


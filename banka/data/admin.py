from django.contrib import admin
from .models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['CustomerId', 'Surname','Exited']
    list_display_links = ['CustomerId', 'Exited']
    list_filter = ['CustomerId']
    search_fields = ['CustomerId', 'Exited']
    #list_editable = ['']
    class Meta:
        model = Data

admin.site.register(Data, DataAdmin)
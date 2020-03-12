from django.contrib import admin
from .models import Events

@admin.register(Events)
class Events(admin.ModelAdmin):
     list_display = ('start','name')

# Register your models here.
#admin.site.register(Events)
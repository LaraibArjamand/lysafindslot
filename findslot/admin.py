from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CalendarEvents)
admin.site.register(CalendarList)
admin.site.register(Holiday)
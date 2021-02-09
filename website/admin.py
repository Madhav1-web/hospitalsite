from django.contrib import admin
from .models import Form, categories, Doctors, News, timeslot

admin.site.register(Form)
admin.site.register(categories)
admin.site.register(Doctors)
admin.site.register(News)
admin.site.register(timeslot)
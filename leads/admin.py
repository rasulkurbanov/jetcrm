from django.contrib import admin

from leads.models import Agent, Lead, User

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
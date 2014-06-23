from django.contrib import admin
from events.models import CredentialsModel

class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)


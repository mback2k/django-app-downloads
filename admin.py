# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Application, Flavor, Version

class ApplicationAdmin(admin.ModelAdmin):
    pass

class FlavorAdmin(admin.ModelAdmin):
    pass

class VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Version, VersionAdmin)

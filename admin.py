# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Commit, Build, Tag

class CommitAdmin(admin.ModelAdmin):
    pass

class BuildAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Commit, CommitAdmin)
admin.site.register(Build, BuildAdmin)
admin.site.register(Tag, TagAdmin)

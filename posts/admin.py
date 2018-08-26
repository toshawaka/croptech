from django.contrib import admin
from . import models

# Register your models here.

class TagInline(admin.TabularInline):
    model = models.Technote.tag.through

class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('tag',)

admin.site.register(models.Tag)
admin.site.register(models.Technote, PostAdmin)
admin.site.register(models.Dictionary)
admin.site.register(models.Researchers)

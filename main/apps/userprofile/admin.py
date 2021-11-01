from django.contrib import admin

from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "birth_date")

    search_fields = ["user__username"]

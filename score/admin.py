from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "points",
    ]
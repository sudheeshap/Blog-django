
from blogapp.models import *
from django.contrib import admin
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

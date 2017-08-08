from django.contrib import admin

# Register your models here.
from .models import Professor
from .models import Subject_area
admin.site.register(Professor)
admin.site.register(Subject_area)
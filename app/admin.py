from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Module)
admin.site.register(models.Course)
admin.site.register(models.Tag)
admin.site.register(models.Institution)
admin.site.register(models.Review)
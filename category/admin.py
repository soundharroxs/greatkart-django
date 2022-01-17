from django.contrib import admin
from . import models

# Register your models here.
class categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("category_name",)}
admin.site.register(models.Category,categoryadmin)
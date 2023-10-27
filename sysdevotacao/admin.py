from django.contrib import admin
from .models import turmas
# Register your models here.
@admin.register(turmas)
class turmasAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

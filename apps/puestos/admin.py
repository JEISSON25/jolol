from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(PuestoVotacion)
class PuestoVotacionAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'state', 'sincro', 'config', 'empresa')

@admin.register(DetailPuestoVotacion)
class DetailPuestoVotacionAdmin(ImportExportModelAdmin):
    list_display = ('puesto', 'mesa')
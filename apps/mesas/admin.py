from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Mesa

@admin.register(Mesa)
class MesaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'empresa')

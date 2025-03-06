from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'state', 'public')

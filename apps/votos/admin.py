from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Voto

@admin.register(Voto)
class VotoAdmin(ImportExportModelAdmin):
    list_display = ('estudiante', 'mesa', 'empresa', 'fechaHora')

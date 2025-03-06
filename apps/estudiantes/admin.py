from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(ImportExportModelAdmin):
    list_display = ('documento', 'nombres', 'apellidos', 'votado')

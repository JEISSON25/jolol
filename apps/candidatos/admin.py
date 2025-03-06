from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Candidato, TipoEleccion

@admin.register(Candidato)
class CandidatoAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'eleccion', 'empresa', 'tarjeton' ,'votos')


@admin.register(TipoEleccion)
class TipoEleccionAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'descripcion')

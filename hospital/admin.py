from django.contrib import admin
from .models.patients import Patient
from .models.wards import Ward
from .models.diagnoses import Diagnosis


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'diagnosis', 'ward')
    search_fields = ('first_name', 'last_name', 'father_name')


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_count')
    search_fields = ('name',)


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


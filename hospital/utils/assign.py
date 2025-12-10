from django.db import transaction
from django.db.models import Count

from hospital.models.patients import Patient
from hospital.models.wards import Ward


@transaction.atomic
def assign_patient_to_ward(patient: Patient):
    compatible_wards = (
        Ward.objects.annotate(
            patients=Count('patient', distinct=True)
        )
        .filter(patient__diagnosis=patient.diagnosis)
        .order_by('patients')
        .distinct()
    )

    for ward in compatible_wards:
        if ward.patients < ward.max_count:
            patient.ward = ward
            return ward

    empty_wards = (
        Ward.objects.annotate(patients=Count('patient', distinct=True))
        .filter(patients=0)
        .order_by('max_count')
    )

    for ward in empty_wards:
        patient.ward = ward
        return ward

    raise Exception("Нет доступных палат для данного диагноза.")

from django.db import models

from .diagnoses import Diagnosis
from .wards import Ward


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, db_column='diagnosis_id')
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, db_column='ward_id', null=True)

    class Meta:
        db_table = 'people'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.father_name}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name} {self.father_name}'

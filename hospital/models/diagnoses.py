from django.db import models


class Diagnosis(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'diagnosis'

    def __str__(self):
        return self.name

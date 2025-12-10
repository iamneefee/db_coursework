from django.db import models


class Ward(models.Model):
    name = models.CharField(max_length=20)
    max_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'wards'

    def __str__(self):
        return f"{self.name} ({self.max_count})"

from django.db import models

class BloodPressureMeasurement(models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.PositiveIntegerField()
    pressao_sistolica = models.PositiveIntegerField()
    pressao_diastolica = models.PositiveIntegerField()
    data_medicao = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.systolic}/{self.diastolic} mmHg on {self.measurement_date.strftime('%Y-%m-%d %H:%M:%S')}"
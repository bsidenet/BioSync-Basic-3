from django.test import TestCase
from .models import BloodPressureMeasurement

class BloodPressureMeasurementModelTest(TestCase):

    def setUp(self):
        BloodPressureMeasurement.objects.create(
            systolic=120,
            diastolic=80,
            measurement_date='2023-10-01'
        )

    def test_blood_pressure_measurement_creation(self):
        measurement = BloodPressureMeasurement.objects.get(systolic=120)
        self.assertEqual(measurement.diastolic, 80)
        self.assertEqual(str(measurement.measurement_date), '2023-10-01')
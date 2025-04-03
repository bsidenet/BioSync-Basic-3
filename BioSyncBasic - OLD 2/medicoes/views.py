from django.shortcuts import render
from django.http import JsonResponse
from .models import BloodPressureMeasurement

def list_measurements(request):
    measurements = BloodPressureMeasurement.objects.all().values()
    return JsonResponse(list(measurements), safe=False)

def add_measurement(request):
    if request.method == 'POST':
        # Assuming data is sent as JSON
        data = request.POST
        measurement = BloodPressureMeasurement(
            systolic=data.get('systolic'),
            diastolic=data.get('diastolic'),
            pulse=data.get('pulse'),
            date=data.get('date')
        )
        measurement.save()
        return JsonResponse({'status': 'success', 'measurement_id': measurement.id}, status=201)
    return JsonResponse({'status': 'fail'}, status=400)
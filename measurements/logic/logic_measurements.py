from ..models import Measurement


def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement_by_id(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement

def delete_measurement_by_id(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement.delete()

def edit_measurement_by_id(id, value, unit, place):
    measurement = Measurement.objects.get(pk=id)
    measurement.value = value
    measurement.unit = unit
    measurement.place = place
    measurement.save()
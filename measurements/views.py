from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from measurements.logic.logic_measurements import get_all_measurements, get_measurement_by_id, delete_measurement_by_id, \
    edit_measurement_by_id


def get_measurements(req):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')


def get_measurement(req, identifier):
    measurement = get_measurement_by_id(identifier)
    measurement_json = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_json, content_type='application/json')

def delete_measurement(req, identifier):
    info = delete_measurement_by_id(identifier)
    return HttpResponse(f'Se elimino exitosamente la medida de id {identifier}. Info: {info}')

def edit_measurement(req, identifier):
    edit_measurement_by_id(identifier, req.GET.get('value'), req.GET.get('unit'),req.GET.get('place'))
    return HttpResponse(f"Se edito exitosamente la medida de id {identifier}. Info: {[req.GET.get('value'), req.GET.get('unit'),req.GET.get('place')]}")


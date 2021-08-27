from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from variables.logic.logic_variables import get_all_variables


def get_variables(req):
    variables = get_all_variables()
    variable_list = serializers.serialize('json', variables)
    return HttpResponse(variable_list, content_type='application/json')
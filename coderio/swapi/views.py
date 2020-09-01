from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from django.db.models import Avg, Max
from swapi.models import Swapi
from swapi.serializers import SwapiSerializer
from rest_framework.decorators import api_view

import requests
import json

def get_data(idcharacter):
    return json.loads(requests.get('https://swapi.dev/api/people/' + str(idcharacter)).text)

@api_view(['GET', 'POST'])
def get_character(request, idcharacter):
    data = get_data(idcharacter)
    # Si idcharacter es inválido idcharacter el mensaje de la API
    if 'detail' in data:
        return JsonResponse(data, safe = False)

    data['average_rating'] = Swapi.objects.filter(idcharacter = idcharacter).aggregate(Avg('rating')).get('rating__avg', 0.00)
    data['max_rating'] = Swapi.objects.filter(idcharacter = idcharacter).aggregate(Max('rating')).get('rating__max', 0.00)
    return JsonResponse(data, safe = False)

def post_character(request, idcharacter, rating):
    data_swapi = get_data(idcharacter)
    if 'detail' in data_swapi:
        return JsonResponse(data_swapi, safe = False)

    data = {'idcharacter': idcharacter, 'rating': rating}
    serializer = SwapiSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        insert = Swapi(idcharacter = data['idcharacter'], rating = data['rating'])
        insert.save()
        data['messsage'] = 'Successful registration'
        return JsonResponse(data, safe = False)
    return JsonResponse(serializer.errors, safe = False)

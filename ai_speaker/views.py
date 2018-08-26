from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return HttpResponse('This pase is first view page.')

@csrf_exempt
def say_hello_world(request):
    output = {
            "speech": 'Hellow World!',
    }
    json_str = json.dumps(output, ensure_ascii=False)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8')

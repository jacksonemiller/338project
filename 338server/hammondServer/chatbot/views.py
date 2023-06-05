from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bot import go

@csrf_exempt
def index(request):
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        return HttpResponse(go(data))
    return HttpResponse("Hello, world. You're at the polls index.")

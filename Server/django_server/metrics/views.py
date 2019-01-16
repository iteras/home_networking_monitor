from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the metrics index.")


def sbc_temperature(request,sbc_id):
    response = "SBC: %s"
    return HttpResponse(response % sbc_id)

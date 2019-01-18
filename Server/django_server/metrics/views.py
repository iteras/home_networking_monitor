from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import SBC


def index(request):
    return HttpResponse("Hello, world. You're at the metrics index.")


def sbc_temperature(request, sbc_id):
    response = "SBC: %s"
    return HttpResponse(response % sbc_id)


def sbc_temperature_data(request, sbc_id):
    SBC_list = SBC.objects.order_by("ts")
#    output = "".join([str(s) for s in SBC_list])
    template = loader.get_template('metrics/index.html')
    context = {
        'SBC_list': SBC_list,
    }
    return HttpResponse(template.render(context, request))

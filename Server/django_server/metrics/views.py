# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from pygal.style import DarkStyle
import pygal, json

from .charts import SBCPieChart, SBCLineChart
from .models import SBC


def index(request):
    return HttpResponse("Hello, world. You're at the metrics index.")


def sbc_temperature(request, sbc_id):
    response = "SBC: %s"
    return HttpResponse(response % sbc_id)


def sbc_post(request):
    if request.method == 'GET':
        return HttpResponse("This url does not support REST GET")
    elif request.method == 'POST':
#        data = request.body.decode("utf-8")
        data = json.loads(request.body.decode("UTF-8"))
        print(data)
#        list = []
#        list.append(request)
#        response = {"response": list}
        response = request.POST.get('Hello')
        return HttpResponse(response)


def sbc_temperature_data(request, sbc_id):
    SBC_list = SBC.objects.order_by("ts")
    template = loader.get_template('metrics/index.html')
    context = {
        'SBC_list': SBC_list,
    }
    return HttpResponse(template.render(context, request))


def sbc_linechart(request):
    template = loader.get_template('metrics/index.html')
    cht_sbc = SBCLineChart(
        height=750,
        width=2000,
        x_label_rotation=20

    )
    context = {'cht_sbc' : cht_sbc.generate()}
    return HttpResponse(template.render(context,request))

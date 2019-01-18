# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from pygal.style import DarkStyle

from .charts import SBCPieChart
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


def sbc_piechart(request):
#    template_name = 'index.html'
    template = loader.get_template('metrics/index.html')


    cht_sbc = SBCPieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )
    context = {'cht_sbc' : cht_sbc.generate()}
    return HttpResponse(template.render(context,request))

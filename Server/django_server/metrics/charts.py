import pygal, time, datetime
from .models import SBC


class SBCPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'SBC temperature'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for sbc in SBC.objects.all():
            data["temperature"] = sbc.temperature
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)


class SBCLineChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Line(**kwargs)
        self.chart.title = 'SBC temperature'

    def get_data(self,type):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        list = []
        segment=10 #sec
        time_range = 20 * 60 # Timerange shown data on graph
        ts_threshold = time.time() - time_range
        sbc_objects = SBC.objects.filter(ts__gte=ts_threshold)
        for sbc in sbc_objects:
            if type == "data":
                list.append(sbc.temperature)
            elif type == "x_labels":
                clock_time = datetime.datetime.fromtimestamp(sbc.ts).time() #ts to readable clock time
                list.append(clock_time)

        if type == "data":
            data["temperature"] = list
            return data
        elif type == "x_labels":
            data = map(str, list)
            return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data("data")
        self.chart.x_labels = self.get_data("x_labels")

        # Add data to chart
        if chart_data is not None:
            for key, value in chart_data.items():
                self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)
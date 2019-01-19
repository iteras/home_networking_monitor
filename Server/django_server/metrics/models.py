from django.db import models
import json


# Create your models here.
class SBC(models.Model):
    temperature = models.FloatField(default=0)
    ts = models.FloatField(default=-1)

    def __str__(self):
        data = {
            'ts': self.ts,
            'temperature': self.temperature}
        s = json.dumps(data)
        return s


class Room_environment(models.Model):
    sbc = models.ForeignKey(SBC,on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    room = models.CharField(max_length=16)
    temperature = models.FloatField(default=-1)
    humidity = models.FloatField(default=-1)
    ts = models.FloatField(default=-1)

    def __str__(self):
        data = {'address': self.address,
                'room': self.address,
                'temperature': self.temperature,
#                'ts': self.ts,
                'humidity': self.humidity}
        s = json.dumps(data)
        return s
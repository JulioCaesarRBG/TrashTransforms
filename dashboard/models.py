from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField()
    distance = models.FloatField()
    mq4 = models.IntegerField()
    mq135 = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Distance: {self.distance} cm"

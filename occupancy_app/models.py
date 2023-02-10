from django.db import models

class PeopleCounter(models.Model):
    sensor_name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=False)
    inside = models.IntegerField()
    out = models.IntegerField()
    
    def __str__(self):
        return f"{self.timestamp} - {self.inside} - {self.out}"

class Sensor(models.Model):
    sensor_name = models.CharField(max_length=50)
    people_counter = models.ManyToManyField(PeopleCounter, related_name='sensors')

    def __str__(self):
        return self.sensor_name
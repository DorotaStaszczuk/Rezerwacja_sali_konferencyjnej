from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField(null=True)
    projector = models.BooleanField(default=True)


class Reservation(models.Model):
    date = models.DateField(unique_for_date=True)
    comment = models.CharField(max_length=200)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)

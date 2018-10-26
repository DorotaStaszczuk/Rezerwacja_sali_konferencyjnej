from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")
    capacity = models.IntegerField(null=True, verbose_name="pojemność")
    projector = models.BooleanField(default=True, verbose_name="rzutnik")


class Reservation(models.Model):
    date = models.DateField(unique_for_date=True, verbose_name="data")
    comment = models.CharField(max_length=200, verbose_name="komentarz")
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)

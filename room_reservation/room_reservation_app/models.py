from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    is_projector_available = models.BooleanField(default=False)
    
    
class RoomReservation(models.Model):
    date = models.DateField()
    comment = models.TextField(null=True, max_length=255)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('date', 'room_id')

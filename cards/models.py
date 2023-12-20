from django.db import models
from django.utils import timezone

from accounts.models import User 

class Calendar(models.Model):
    name = models.CharField(max_length = 255)
    created_by = models.ForeignKey(User, related_name='calendars', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at', ) #- for descending

class Card(models.Model):
    calendar = models.ForeignKey(Calendar, related_name='cards', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ordering = models.IntegerField()
    text = models.TextField()
    available_at = models.DateTimeField()
    style = models.CharField(max_length=255, default='bg-gray-100')

    def is_available(self):
        return self.available_at < timezone.now()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('ordering',)

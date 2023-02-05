from django.db import models
from .Events import Events
from .lecturer import Lecturer


class Event_programs(models.Model):
    """
    Model for creating Event Programs objects that is subset for Events Object
    it can not be used with out a lecturer instance
    # its relation is CASCADE
    """
    Event = models.ForeignKey("Events", on_delete=models.CASCADE)
    Lecturer = models.ForeignKey("Lecturer", on_delete=models.CASCADE)
    Topic = models.CharField(max_length=55)
    Description = models.TextField(blank=True, null=True)
    Session_link = models.URLField(max_length=255, blank=True, null=True)
    
    Available = models.BooleanField(default=True)

    Session_date = models.DateTimeField()
    Created_date = models.DateTimeField(auto_now=True)
    Updated_date = models.DateTimeField(auto_now_add=True)

    def __ste__(self):
        return f"{self.Event.Title}, {self.Lecturer.Name}, {self.Available}, {self.Created_date}, {self.Updated_date}"

from django.db import models

"""
The Event App database models
"""


class Events (models.Model):
    """
    Model for objects in Events Table
    Contains the information about Events
    # only Superuser can add or change the objects.
    """
    Category = models.ForeignKey("Category", on_delete=models.CASCADE, default=None)
    Title = models.CharField(max_length=50)
    Image = models.URLField(max_length=255, null= True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Capacity = models.IntegerField(blank=True, null=True)
    Registration_onset = models.DateTimeField()
    Registration_end = models.DateTimeField()
    Event_onset = models.DateTimeField()
    Event_end = models.DateTimeField()
    Is_published = models.BooleanField(default=False)
    Expired = models.BooleanField(default=False)
    Published_data = models.DateTimeField()
    Created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.Title}, {self.Category.Name}, {self.Capacity}"


class Category(models.Model):
    """
    The Categories of Events
    # only Superuser can add or change the objects.
    """
    Name = models.CharField(max_length=55)

    def __str__(self):
        return self.Name
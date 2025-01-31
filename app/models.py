from django.db import models
from django.conf import settings


# User model (Equivalent to Author)
class User(models.Model):
    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('business', 'Business'),
        ('admin', 'Administrator'),
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return self.username


# Location model (Equivalent to Store)
class Location(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.address


# GarbageType model (Equivalent to Publisher)
class GarbageType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# GarbageSchedule model (Equivalent to Book)
class GarbageSchedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    collection_date = models.DateField()
    time_slot = models.TimeField()

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('missed', 'Missed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    garbage_type = models.ManyToManyField(GarbageType)

    def __str__(self):
        return f"Collection at {self.location.address} on {self.collection_date}"

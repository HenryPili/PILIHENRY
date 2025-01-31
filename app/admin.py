from django.contrib import admin
from .models import GarbageSchedule, GarbageType, Location, User

admin.site.register(GarbageSchedule)
admin.site.register(GarbageType)
admin.site.register(Location)
admin.site.register(User)


from django.contrib import admin
from .models import Cows
from .models import BornCows
from .models import photo
# Register your models here.
admin.site.register(Cows)
admin.site.register(BornCows)
admin.site.register(photo)


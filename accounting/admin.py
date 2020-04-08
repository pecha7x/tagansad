from django.contrib import admin

from .models import PlantKind
from .models import Plant

admin.site.register(PlantKind)
admin.site.register(Plant)
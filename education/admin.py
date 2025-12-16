from django.contrib import admin
from .models import (
    MasterPrograms,
    CollegePrograms,
    PhdPrograms,
)

# Register existing models
admin.site.register(MasterPrograms)
admin.site.register(CollegePrograms)
admin.site.register(PhdPrograms)

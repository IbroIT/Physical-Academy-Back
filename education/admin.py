from django.contrib import admin
from .models import FacultyTeachers, MasterPrograms, Faculty, FacultyContacts, FacultyStatistics, FacultySports, FacultyPrograms, FacultySpecialization, CollegePrograms, PhdPrograms

# Register your models here.
admin.site.register(MasterPrograms)
admin.site.register(FacultyTeachers)
admin.site.register(Faculty)
admin.site.register(FacultySpecialization)
admin.site.register(FacultyPrograms)
admin.site.register(FacultySports)
admin.site.register(FacultyContacts)
admin.site.register(FacultyStatistics)
admin.site.register(CollegePrograms)
admin.site.register(PhdPrograms)

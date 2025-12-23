from django.contrib import admin
from .models import (
    MasterTabCategory,
    MasterDepartmentInfo,
    MasterManagement,
    PhdManagement,
    PhdTabCategory,
    PhdDepartmentInfo,
    CollegeDepartmentInfo,
    CollegeTabCategory,
    CollegeManagement,
)

# Register existing models
admin.site.register(MasterTabCategory)
admin.site.register(MasterDepartmentInfo)
admin.site.register(MasterManagement)
admin.site.register(PhdTabCategory)
admin.site.register(PhdDepartmentInfo)
admin.site.register(PhdManagement)
admin.site.register(CollegeTabCategory)
admin.site.register(CollegeDepartmentInfo)
admin.site.register(CollegeManagement)

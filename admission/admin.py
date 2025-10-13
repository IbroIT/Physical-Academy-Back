from django.contrib import admin
from .models import (
    BachelorProgram,
    CollegeAdmissionSteps, CollegePrograms, CollegeStatistics, DoctorAdmissionSteps, QuotaType, QuotaRequirement, QuotaBenefit, 
    QuotaStats, AdditionalSupport, ProcessStep,
    AspirantRequirements, AspirantMainDate, AspirantDocuments, AspirantPrograms,
    MasterDocuments, MasterRequirements, MasterPrograms, MasterMainDate,
    DoctorStatistics, DoctorPrograms, DoctorAdmissionSteps, CollegeSoonEvents, CollegeAdmissionRequirements
)

admin.site.register(BachelorProgram)


class QuotaRequirementInline(admin.TabularInline):
    """Inline админка для требований к квотам"""
    model = QuotaRequirement
    extra = 1
    fields = ('requirement_ru', 'requirement_ky', 'requirement_en', 'order', 'is_active')


class QuotaBenefitInline(admin.TabularInline):
    """Inline админка для преимуществ квот"""
    model = QuotaBenefit
    extra = 1
    fields = ('benefit_ru', 'benefit_ky', 'benefit_en', 'order', 'is_active')


@admin.register(QuotaType)
class QuotaTypeAdmin(admin.ModelAdmin):
    """Админка для типов квот"""
    list_display = ['type', 'title_ru', 'spots', 'deadline', 'color', 'is_active', 'order']
    list_filter = ['color', 'is_active', 'type']
    search_fields = ['title_ru', 'title_ky', 'title_en', 'description_ru']
    list_editable = ['order', 'is_active', 'spots']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('type', 'icon', 'spots', 'deadline', 'color', 'order', 'is_active')
        }),
        ('Название на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )
    
    inlines = [QuotaRequirementInline, QuotaBenefitInline]


@admin.register(QuotaRequirement)
class QuotaRequirementAdmin(admin.ModelAdmin):
    """Админка для требований к квотам"""
    list_display = ['quota_type', 'requirement_ru_short', 'order', 'is_active']
    list_filter = ['quota_type', 'is_active']
    search_fields = ['requirement_ru', 'requirement_ky', 'requirement_en']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('quota_type', 'order', 'is_active')
        }),
        ('Требования на языках', {
            'fields': ('requirement_ru', 'requirement_ky', 'requirement_en')
        }),
    )
    
    def requirement_ru_short(self, obj):
        """Сокращенное отображение требования"""
        return obj.requirement_ru[:50] + "..." if len(obj.requirement_ru) > 50 else obj.requirement_ru
    requirement_ru_short.short_description = 'Требование (рус.)'


@admin.register(QuotaBenefit)
class QuotaBenefitAdmin(admin.ModelAdmin):
    """Админка для преимуществ квот"""
    list_display = ['quota_type', 'benefit_ru_short', 'order', 'is_active']
    list_filter = ['quota_type', 'is_active']
    search_fields = ['benefit_ru', 'benefit_ky', 'benefit_en']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('quota_type', 'order', 'is_active')
        }),
        ('Преимущества на языках', {
            'fields': ('benefit_ru', 'benefit_ky', 'benefit_en')
        }),
    )
    
    def benefit_ru_short(self, obj):
        """Сокращенное отображение преимущества"""
        return obj.benefit_ru[:50] + "..." if len(obj.benefit_ru) > 50 else obj.benefit_ru
    benefit_ru_short.short_description = 'Преимущество (рус.)'


@admin.register(QuotaStats)
class QuotaStatsAdmin(admin.ModelAdmin):
    """Админка для статистики квот"""
    list_display = ['stat_type', 'number', 'label_ru', 'order', 'is_active']
    list_filter = ['stat_type', 'is_active']
    search_fields = ['label_ru', 'label_ky', 'label_en']
    list_editable = ['order', 'is_active', 'number']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('stat_type', 'number', 'order', 'is_active')
        }),
        ('Подписи на языках', {
            'fields': ('label_ru', 'label_ky', 'label_en')
        }),
        ('Описания на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )


@admin.register(AdditionalSupport)
class AdditionalSupportAdmin(admin.ModelAdmin):
    """Админка для дополнительной поддержки"""
    list_display = ['support_ru_short', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['support_ru', 'support_ky', 'support_en']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('order', 'is_active')
        }),
        ('Поддержка на языках', {
            'fields': ('support_ru', 'support_ky', 'support_en')
        }),
    )
    
    def support_ru_short(self, obj):
        """Сокращенное отображение поддержки"""
        return obj.support_ru[:50] + "..." if len(obj.support_ru) > 50 else obj.support_ru
    support_ru_short.short_description = 'Поддержка (рус.)'


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    """Админка для шагов процесса"""
    list_display = ['step_number', 'title_ru', 'color_scheme', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_ky', 'title_en', 'description_ru']
    list_editable = ['is_active']
    ordering = ['step_number']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('step_number', 'color_scheme', 'is_active')
        }),
        ('Названия на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описания на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )

@admin.register(AspirantRequirements)
class AspirantRequirementsAdmin(admin.ModelAdmin):
    """Админка для требований к аспирантуре"""
    list_display = ['title_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_ky', 'title_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )
    

@admin.register(AspirantMainDate)
class AspirantMainDateAdmin(admin.ModelAdmin):
    """Админка для основных дат аспирантуры"""
    list_display = ['event_name_ru', 'date', 'is_active']
    list_filter = ['is_active']
    search_fields = ['event_name_ru', 'event_name_ky', 'event_name_en']
    list_editable = ['is_active', 'date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('date', 'is_active')
        }),
        ('Название события на языках', {
            'fields': ('event_name_ru', 'event_name_ky', 'event_name_en')
        }),
        ('Описание события на языках', {
            'fields': ('event_description_ru', 'event_description_ky', 'event_description_en')
        }),
    )
@admin.register(AspirantDocuments)
class AspirantDocumentsAdmin(admin.ModelAdmin):
    """Админка для документов аспирантуры"""
    list_display = ['document_name_ru', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['document_name_ru', 'document_name_ky', 'document_name_en']
    list_editable = ['is_active', 'order']
    ordering = ['order']

    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active', 'order', 'file')
        }),
        ('Название документа на языках', {
            'fields': ('document_name_ru', 'document_name_ky', 'document_name_en')
        }),
       
    )

    readonly_fields = ('created_at', 'updated_at')



@admin.register(AspirantPrograms)
class AspirantProgramsAdmin(admin.ModelAdmin):
    """Админка для программ аспирантуры"""
    list_display = ['program_name_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['program_name_ru', 'program_name_ky', 'program_name_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название программы на языках', {
            'fields': ('program_name_ru', 'program_name_ky', 'program_name_en')
        }),
        ('Описание программы на языках', {
            'fields': ('program_description_ru', 'program_description_ky', 'program_description_en')
        }),
    )


@admin.register(MasterPrograms)
class MasterProgramsAdmin(admin.ModelAdmin):
    """Админка для программ магистратуры"""
    list_display = ['program_name_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['program_name_ru', 'program_name_ky', 'program_name_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название программы на языках', {
            'fields': ('program_name_ru', 'program_name_ky', 'program_name_en')
        }),
        ('Описание программы на языках', {
            'fields': ('program_description_ru', 'program_description_ky', 'program_description_en')
        }),
    )


@admin.register(MasterDocuments)
class MasterDocumentsAdmin(admin.ModelAdmin):
    """Админка для документов магистратуры"""
    list_display = ['document_name_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['document_name_ru', 'document_name_ky', 'document_name_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название документа на языках', {
            'fields': ('document_name_ru', 'document_name_ky', 'document_name_en')
        }),
     
    )



@admin.register(MasterMainDate)
class MasterMainDateAdmin(admin.ModelAdmin):
    """Админка для основных дат магистратуры"""
    list_display = ['event_name_ru', 'date', 'is_active']
    list_filter = ['is_active']
    search_fields = ['event_name_ru', 'event_name_ky', 'event_name_en']
    list_editable = ['is_active', 'date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('date', 'is_active')
        }),
        ('Название события на языках', {
            'fields': ('event_name_ru', 'event_name_ky', 'event_name_en')
        }),
        ('Описание события на языках', {
            'fields': ('event_description_ru', 'event_description_ky', 'event_description_en')
        }),
    )

@admin.register(MasterRequirements)
class MasterRequirementsAdmin(admin.ModelAdmin):
    """Админка для требований к магистратуре"""
    list_display = ['title_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_ky', 'title_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )

@admin.register(DoctorStatistics)
class DoctorStatisticsAdmin(admin.ModelAdmin):
    """Админка для статистики докторантуры"""
    list_display = ['titleInt']

    fieldsets = (
        ('Основная информация', {
            'fields': ('titleInt',)
        }),
        ('Описания на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )

@admin.register(DoctorPrograms)
class DoctorProgramsAdmin(admin.ModelAdmin):
    """Админка для программ докторантуры"""
    list_display = ['program_name_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['program_name_ru', 'program_name_ky', 'program_name_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название программы на языках', {
            'fields': ('program_name_ru', 'program_name_ky', 'program_name_en')
        }),
        ('Описание программы на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
        ('Короткое описание программы на языках', {
            'fields': ('short_description_ru', 'short_description_ky', 'short_description_en')
        }),
        ('Длительность(годы)', {'fields': ('duration',)}
         ),
        ('Особенности программы на языках', {
            'fields': ('features_ru', 'features_ky', 'features_en')
        }),
    )

@admin.register(DoctorAdmissionSteps)
class DoctorAdmissionStepsAdmin(admin.ModelAdmin):
    """Админка для шагов приема в докторантуру"""
    list_display = ['title_ru',  'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_ky', 'title_en']
    list_editable = ['is_active']
    ordering = ['order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('order',  'is_active')
        }),
        ('Название шага на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание шага на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
        ('Требования шага на языках', {
            'fields': ('requirement_ru', 'requirement_ky', 'requirement_en')
        }),
        ('дедлайн на языках', {
            'fields': ('deadline_ru', 'deadline_ky', 'deadline_en')
        }),
    )


@admin.register(CollegeSoonEvents)
class CollegeSoonEventsAdmin(admin.ModelAdmin):
    """Админка для предстоящих событий колледжа"""
    list_display = ['event_ru', 'date', 'is_active']
    list_filter = ['is_active']
    search_fields = ['event_ru', 'event_ky', 'event_en']
    list_editable = ['is_active', 'date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('date', 'is_active')
        }),
        ('Название события на языках', {
            'fields': ('event_ru', 'event_ky', 'event_en')
        }),
    )
    
    
@admin.register(CollegeAdmissionSteps)
class CollegeAdmissionStepsAdmin(admin.ModelAdmin):
    """Админка для шагов приема в колледж"""
    list_display = ['title_ru',]
    search_fields = ['title_ru', 'title_ky', 'title_en']
    ordering = ['order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('order', )
        }),
        ('Название шага на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание шага на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
        ('длительность на языках', {
            'fields': ('duration_ru', 'duration_ky', 'duration_en')
        }),
    )


@admin.register(CollegeAdmissionRequirements)
class CollegeAdmissionRequirementsAdmin(admin.ModelAdmin):
    """Админка для требований к колледжу"""
    list_display = ['title_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_ky', 'title_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название на языках', {
            'fields': ('title_ru', 'title_ky', 'title_en')
        }),
        ('Описание на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )


@admin.register(CollegeStatistics)
class CollegeStatisticsAdmin(admin.ModelAdmin):
    """Админка для статистики колледжа"""
    list_display = ['titleInt']

    fieldsets = (
        ('Основная информация', {
            'fields': ('titleInt',)
        }),
        ('Описания на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
    )

@admin.register(CollegePrograms)
class CollegeProgramsAdmin(admin.ModelAdmin):
    """Админка для программ колледжа"""
    list_display = ['program_name_ru', 'is_active']
    list_filter = ['is_active']
    search_fields = ['program_name_ru', 'program_name_ky', 'program_name_en']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('is_active',)
        }),
        ('Название программы на языках', {
            'fields': ('program_name_ru', 'program_name_ky', 'program_name_en')
        }),
        ('Описание программы на языках', {
            'fields': ('description_ru', 'description_ky', 'description_en')
        }),
        ('Короткое описание программы на языках', {
            'fields': ('short_description_ru', 'short_description_ky', 'short_description_en')
        }),
        ('Длительность(годы)', {'fields': ('duration',)}
         ),
        ('Особенности программы на языках', {
            'fields': ('features_ru', 'features_ky', 'features_en')
        }),
    )

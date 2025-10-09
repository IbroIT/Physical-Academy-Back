from rest_framework import serializers
from .models import (
    BoardOfTrustees, AuditCommission, AcademicCouncil,
    TradeUnionBenefit, TradeUnionEvent, TradeUnionStats,
    Commission, AdministrativeDepartment, AdministrativeUnit,
    BoardOfTrusteesStats, AuditCommissionStatistics,
    Leadership, OrganizationStructure, Document
)


class MultiLanguageSerializerMixin:
    """Mixin for handling multi-language fields"""
    
    def get_language(self):
        """Get language from request context"""
        request = self.context.get('request')
        if request:
            # Check query parameter first
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                # Check Accept-Language header
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language.lower():
                    language = 'en'
                elif 'ky' in accept_language.lower() or 'kg' in accept_language.lower():
                    language = 'kg'
            return language
        return 'ru'
    
    def get_translated_field(self, obj, field_name):
        """Get field value in the requested language"""
        language = self.get_language()
        
        if language == 'kg':
            translated_value = getattr(obj, f'{field_name}_kg', None)
            if translated_value:
                return translated_value
        elif language == 'en':
            translated_value = getattr(obj, f'{field_name}_en', None)
            if translated_value:
                return translated_value
        
        # Fallback to Russian
        return getattr(obj, field_name)
    
    def get_translated_json_field(self, obj, field_name):
        """Get JSON field value in the requested language"""
        language = self.get_language()
        
        if language == 'kg':
            translated_value = getattr(obj, f'{field_name}_kg', None)
            if translated_value and len(translated_value) > 0:
                return translated_value
        elif language == 'en':
            translated_value = getattr(obj, f'{field_name}_en', None)
            if translated_value and len(translated_value) > 0:
                return translated_value
        
        # Fallback to Russian
        return getattr(obj, field_name, [])


class BoardOfTrusteesSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Board of Trustees"""
    
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = BoardOfTrustees
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'position', 'position_kg', 'position_en',
            'bio', 'bio_kg', 'bio_en',
            'achievements', 'achievements_kg', 'achievements_en',
            'email', 'phone', 'image', 'image_url', 'icon', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_position(self, obj):
        return self.get_translated_field(obj, 'position')
    
    def get_bio(self, obj):
        return self.get_translated_field(obj, 'bio')
    
    def get_achievements(self, obj):
        return self.get_translated_json_field(obj, 'achievements')
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class BoardOfTrusteesStatsSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Board of Trustees Statistics"""
    
    label = serializers.SerializerMethodField()
    value = serializers.IntegerField(source='target_value')  # Rename target_value to value for frontend
    color = serializers.SerializerMethodField()
    
    class Meta:
        model = BoardOfTrusteesStats
        fields = ['id', 'label', 'value', 'icon', 'color', 'order']
    
    def get_label(self, obj):
        return self.get_translated_field(obj, 'label')
    
    def get_color(self, obj):
        return f"from-{obj.color_from} to-{obj.color_to}"


class AuditCommissionSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Audit Commission"""
    
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = AuditCommission
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'position', 'position_kg', 'position_en',
            'department', 'department_kg', 'department_en',
            'achievements', 'achievements_kg', 'achievements_en',
            'email', 'phone', 'image', 'image_url', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_position(self, obj):
        return self.get_translated_field(obj, 'position')
    
    def get_department(self, obj):
        return self.get_translated_field(obj, 'department')
    
    def get_achievements(self, obj):
        return self.get_translated_json_field(obj, 'achievements')
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class AuditCommissionStatisticsSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Audit Commission Statistics"""
    
    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    
    class Meta:
        model = AuditCommissionStatistics
        fields = ['id', 'label', 'label_kg', 'label_en', 'value', 'value_kg', 'value_en', 'icon', 'order']
    
    def get_label(self, obj):
        return self.get_translated_field(obj, 'label')
    
    def get_value(self, obj):
        return self.get_translated_field(obj, 'value')


class AcademicCouncilSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Academic Council"""
    
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = AcademicCouncil
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'position', 'position_kg', 'position_en',
            'department', 'department_kg', 'department_en',
            'achievements', 'achievements_kg', 'achievements_en',
            'email', 'phone', 'image', 'image_url', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_position(self, obj):
        return self.get_translated_field(obj, 'position')
    
    def get_department(self, obj):
        return self.get_translated_field(obj, 'department')
    
    def get_achievements(self, obj):
        return self.get_translated_json_field(obj, 'achievements')
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class TradeUnionBenefitSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Trade Union Benefits"""
    
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = TradeUnionBenefit
        fields = [
            'id', 'title', 'title_kg', 'title_en',
            'description', 'description_kg', 'description_en',
            'icon', 'order'
        ]
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')


class TradeUnionEventSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Trade Union Events"""
    
    title = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = TradeUnionEvent
        fields = [
            'id', 'title', 'title_kg', 'title_en',
            'date', 'date_kg', 'date_en',
            'description', 'description_kg', 'description_en',
            'image', 'image_url', 'icon', 'order'
        ]
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_date(self, obj):
        return self.get_translated_field(obj, 'date')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None


class TradeUnionStatsSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Trade Union Statistics"""
    
    label = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    
    class Meta:
        model = TradeUnionStats
        fields = ['id', 'label', 'label_kg', 'label_en', 'value', 'icon', 'color', 'order']
    
    def get_label(self, obj):
        return self.get_translated_field(obj, 'label')
    
    def get_color(self, obj):
        return f"from-{obj.color_from} to-{obj.color_to}"


class CommissionSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Commissions"""
    
    name = serializers.SerializerMethodField()
    chairman = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()
    responsibilities = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = Commission
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'chairman', 'chairman_kg', 'chairman_en',
            'description', 'description_kg', 'description_en',
            'members', 'members_kg', 'members_en',
            'responsibilities', 'responsibilities_kg', 'responsibilities_en',
            'category', 'category_display', 'icon',
            'email', 'phone', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_chairman(self, obj):
        return self.get_translated_field(obj, 'chairman')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_members(self, obj):
        return self.get_translated_json_field(obj, 'members')
    
    def get_responsibilities(self, obj):
        return self.get_translated_json_field(obj, 'responsibilities')


class AdministrativeDepartmentSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Administrative Departments"""
    
    name = serializers.SerializerMethodField()
    head = serializers.SerializerMethodField()
    responsibilities = serializers.SerializerMethodField()
    
    class Meta:
        model = AdministrativeDepartment
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'head', 'head_kg', 'head_en',
            'responsibilities', 'responsibilities_kg', 'responsibilities_en',
            'email', 'phone', 'icon', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_head(self, obj):
        return self.get_translated_field(obj, 'head')
    
    def get_responsibilities(self, obj):
        return self.get_translated_json_field(obj, 'responsibilities')


class AdministrativeUnitSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for Administrative Units"""
    
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    head = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()
    responsibilities = serializers.SerializerMethodField()
    
    class Meta:
        model = AdministrativeUnit
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'description', 'description_kg', 'description_en',
            'head', 'head_kg', 'head_en',
            'location', 'location_kg', 'location_en',
            'staff', 'staff_kg', 'staff_en',
            'responsibilities', 'responsibilities_kg', 'responsibilities_en',
            'email', 'phone', 'icon', 'color', 'color_class', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_head(self, obj):
        return self.get_translated_field(obj, 'head')
    
    def get_location(self, obj):
        return self.get_translated_field(obj, 'location')
    
    def get_staff(self, obj):
        return self.get_translated_field(obj, 'staff')
    
    def get_responsibilities(self, obj):
        return self.get_translated_json_field(obj, 'responsibilities')


# ========== NEW SERIALIZERS FOR MISSING APIs ==========

class LeadershipSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Сериалайзер для Leadership (для /leadership/)"""
    
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    
    class Meta:
        model = Leadership
        fields = [
            'id', 'name', 'position', 'leadership_type', 'department',
            'bio', 'achievements', 'education', 'email', 'phone',
            'image', 'experience_years', 'icon', 'is_active', 'order'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_position(self, obj):
        return self.get_translated_field(obj, 'position')
    
    def get_department(self, obj):
        return self.get_translated_field(obj, 'department')
    
    def get_bio(self, obj):
        return self.get_translated_field(obj, 'bio')
    
    def get_achievements(self, obj):
        return self.get_translated_json_field(obj, 'achievements')
    
    def get_education(self, obj):
        return self.get_translated_field(obj, 'education')


class OrganizationStructureSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Сериалайзер для OrganizationStructure (для /organization-structure/)"""
    
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    head = serializers.SerializerMethodField()
    responsibilities = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = OrganizationStructure
        fields = [
            'id', 'name', 'structure_type', 'description', 'head',
            'parent', 'responsibilities', 'email', 'phone', 'location',
            'staff_count', 'icon', 'is_active', 'order', 'children'
        ]
    
    def get_name(self, obj):
        return self.get_translated_field(obj, 'name')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_head(self, obj):
        return self.get_translated_field(obj, 'head')
    
    def get_responsibilities(self, obj):
        return self.get_translated_json_field(obj, 'responsibilities')
    
    def get_location(self, obj):
        return self.get_translated_field(obj, 'location')
    
    def get_children(self, obj):
        """Get child structures"""
        children = OrganizationStructure.objects.filter(parent=obj, is_active=True).order_by('order', 'name')
        return OrganizationStructureSerializer(children, many=True, context=self.context).data


class DocumentSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Сериалайзер для Document (для /documents/)"""
    
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    file_size_formatted = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = [
            'id', 'title', 'document_type', 'description', 'file',
            'file_url', 'document_number', 'document_date',
            'file_size', 'file_size_formatted', 'file_format',
            'icon', 'is_active', 'is_featured', 'order'
        ]
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_file_url(self, obj):
        """Get absolute URL for file"""
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None
    
    def get_file_size_formatted(self, obj):
        """Format file size in human readable format"""
        if obj.file_size:
            if obj.file_size < 1024:
                return f"{obj.file_size} B"
            elif obj.file_size < 1024 * 1024:
                return f"{obj.file_size / 1024:.1f} KB"
            else:
                return f"{obj.file_size / (1024 * 1024):.1f} MB"
        return "N/A"

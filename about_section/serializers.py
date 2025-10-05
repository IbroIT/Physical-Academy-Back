from .models import Leadership, Accreditation, OrganizationStructure, DownloadableDocument
from rest_framework import serializers



class LeadershipSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства ВШМ"""
    leadership_type_display = serializers.CharField(source='get_leadership_type_display', read_only=True)
    image_url = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()
    
    class Meta:
        model = Leadership
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'position', 'position_kg', 'position_en',
            'degree', 'degree_kg', 'degree_en',
            'experience', 'experience_kg', 'experience_en',
            'bio', 'bio_kg', 'bio_en',
            'achievements', 'achievements_kg', 'achievements_en',
            'department', 'department_kg', 'department_en',
            'specialization', 'specialization_kg', 'specialization_en',
            'email', 'phone', 'image', 'image_url',
            'leadership_type', 'leadership_type_display',
            'is_director', 'order'
        ]
    
    def get_language(self):
        """Get language from request context"""
        request = self.context.get('request')
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
            return language
        return 'ru'
    
    def get_name(self, obj):
        """Get name in request language"""
        language = self.get_language()
        if language == 'en' and obj.name_en:
            return obj.name_en
        elif language == 'ky' and obj.name_kg:
            return obj.name_kg
        return obj.name
    
    def get_position(self, obj):
        """Get position in request language"""
        language = self.get_language()
        if language == 'en' and obj.position_en:
            return obj.position_en
        elif language == 'ky' and obj.position_kg:
            return obj.position_kg
        return obj.position
    
    def get_degree(self, obj):
        """Get degree in request language"""
        language = self.get_language()
        if language == 'en' and obj.degree_en:
            return obj.degree_en
        elif language == 'ky' and obj.degree_kg:
            return obj.degree_kg
        return obj.degree
    
    def get_experience(self, obj):
        """Get experience in request language"""
        language = self.get_language()
        if language == 'en' and obj.experience_en:
            return obj.experience_en
        elif language == 'ky' and obj.experience_kg:
            return obj.experience_kg
        return obj.experience
    
    def get_bio(self, obj):
        """Get bio in request language"""
        language = self.get_language()
        if language == 'en' and obj.bio_en:
            return obj.bio_en
        elif language == 'ky' and obj.bio_kg:
            return obj.bio_kg
        return obj.bio
    
    def get_achievements(self, obj):
        """Get achievements in request language"""
        language = self.get_language()
        if language == 'en' and obj.achievements_en:
            return obj.achievements_en
        elif language == 'ky' and obj.achievements_kg:
            return obj.achievements_kg
        return obj.achievements
    
    def get_department(self, obj):
        """Get department in request language"""
        language = self.get_language()
        if language == 'en' and obj.department_en:
            return obj.department_en
        elif language == 'ky' and obj.department_kg:
            return obj.department_kg
        return obj.department
    
    def get_specialization(self, obj):
        """Get specialization in request language"""
        language = self.get_language()
        if language == 'en' and obj.specialization_en:
            return obj.specialization_en
        elif language == 'ky' and obj.specialization_kg:
            return obj.specialization_kg
        return obj.specialization
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    

class AccreditationSerializer(serializers.ModelSerializer):
    accreditation_type_display = serializers.CharField(source='get_accreditation_type_display', read_only=True)
    is_valid = serializers.BooleanField(read_only=True)
    certificate_image_url = serializers.SerializerMethodField()
    organization_logo_url = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    organization = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = Accreditation
        fields = '__all__'
    
    def get_language(self):
        """Get language from request context"""
        request = self.context.get('request')
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
            return language
        return 'ru'
    
    def get_name(self, obj):
        """Get name in request language"""
        language = self.get_language()
        if language == 'en' and obj.name_en:
            return obj.name_en
        elif language == 'ky' and obj.name_kg:
            return obj.name_kg
        return obj.name
    
    def get_organization(self, obj):
        """Get organization in request language"""
        language = self.get_language()
        if language == 'en' and obj.organization_en:
            return obj.organization_en
        elif language == 'ky' and obj.organization_kg:
            return obj.organization_kg
        return obj.organization
    
    def get_description(self, obj):
        """Get description in request language"""
        language = self.get_language()
        if language == 'en' and obj.description_en:
            return obj.description_en
        elif language == 'ky' and obj.description_kg:
            return obj.description_kg
        return obj.description

    def get_certificate_image_url(self, obj):
        if obj.certificate_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.certificate_image.url)
            return obj.certificate_image.url
        return None

    def get_organization_logo_url(self, obj):
        if obj.organization_logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.organization_logo.url)
            return obj.organization_logo.url
        return None
    

class OrganizationStructureSerializer(serializers.ModelSerializer):
    """Serializer for OrganizationStructure model with multilingual support"""
    
    name = serializers.SerializerMethodField()
    head_name = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = OrganizationStructure
        fields = [
            'id', 'name', 'name_ru', 'name_en', 'name_ky',
            'head_name', 'head_name_ru', 'head_name_en', 'head_name_ky',
            'structure_type', 'phone', 'email', 'icon', 
            'parent', 'children', 'order', 'is_active', 'title'
        ]
        read_only_fields = ['id', 'name', 'head_name', 'children', 'title']
    
    def get_name(self, obj):
        """Get name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def get_head_name(self, obj):
        """Get head name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_head_name(language)
    
    def get_title(self, obj):
        """Get title for the structure type"""
        return obj.get_structure_type_display()
    
    def get_children(self, obj):
        """Get child departments"""
        children = obj.children.filter(is_active=True).order_by('order')
        if children.exists():
            serializer = OrganizationStructureSerializer(
                children, 
                many=True, 
                context=self.context
            )
            return serializer.data
        return []
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language


class DownloadableDocumentSerializer(serializers.ModelSerializer):
    """Serializer for DownloadableDocument model with multilingual support"""
    
    title = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = DownloadableDocument
        fields = ['id', 'title', 'title_ru', 'title_en', 'title_kg', 'file', 'file_url', 'upload_date']
        read_only_fields = ['id', 'title', 'file_url', 'upload_date']
    
    def get_title(self, obj):
        """Get title in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_title(language)
    
    def get_file_url(self, obj):
        """Get absolute URL for the file"""
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language
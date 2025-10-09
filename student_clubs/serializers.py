from rest_framework import serializers
from .models import Club, ClubCategory, ClubLeader, ClubStats


class ClubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий с поддержкой языков"""
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = ClubCategory
        fields = ['id', 'slug', 'name', 'name_ru', 'name_en', 'name_kg', 'order']
    
    def get_name(self, obj):
        """Возвращает название на языке из контекста запроса"""
        language = self.context.get('language', 'ru')
        return obj.get_name(language)


class ClubLeaderSerializer(serializers.ModelSerializer):
    """Сериализатор руководителей клубов"""
    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    
    class Meta:
        model = ClubLeader
        fields = [
            'id', 'name', 'role', 'email', 'phone', 'photo',
            'name_ru', 'name_en', 'name_kg',
            'role_ru', 'role_en', 'role_kg'
        ]
    
    def get_name(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('name', language)
    
    def get_role(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('role', language)


class ClubListSerializer(serializers.ModelSerializer):
    """Краткий сериализатор для списка клубов"""
    category = ClubCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ClubCategory.objects.all(),
        source='category',
        write_only=True
    )
    
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    meetings = serializers.SerializerMethodField()
    
    class Meta:
        model = Club
        fields = [
            'id', 'category', 'category_id', 'icon', 'status', 
            'members_count', 'name', 'short_description', 
            'description', 'meetings', 'tags', 'join_link',
            'created_at', 'updated_at'
        ]
    
    def get_name(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('name', language)
    
    def get_short_description(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('short_description', language)
    
    def get_description(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('description', language)
    
    def get_meetings(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('meetings', language)


class ClubDetailSerializer(serializers.ModelSerializer):
    """Полный сериализатор клуба со всеми деталями"""
    category = ClubCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ClubCategory.objects.all(),
        source='category',
        write_only=True
    )
    leaders = ClubLeaderSerializer(many=True, read_only=True)
    
    # Локализованные поля
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    goals = serializers.SerializerMethodField()
    motivation = serializers.SerializerMethodField()
    meetings = serializers.SerializerMethodField()
    
    class Meta:
        model = Club
        fields = [
            'id', 'category', 'category_id', 'icon', 'status', 
            'members_count', 'join_link',
            'name', 'short_description', 'description',
            'goals', 'motivation', 'meetings',
            'tags', 'leaders', 'order', 'is_active',
            'created_at', 'updated_at',
            # Все языковые версии для админки
            'name_ru', 'name_en', 'name_kg',
            'short_description_ru', 'short_description_en', 'short_description_kg',
            'description_ru', 'description_en', 'description_kg',
            'goals_ru', 'goals_en', 'goals_kg',
            'motivation_ru', 'motivation_en', 'motivation_kg',
            'meetings_ru', 'meetings_en', 'meetings_kg',
        ]
    
    def get_name(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('name', language)
    
    def get_short_description(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('short_description', language)
    
    def get_description(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('description', language)
    
    def get_goals(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('goals', language)
    
    def get_motivation(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('motivation', language)
    
    def get_meetings(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_field('meetings', language)


class ClubStatsSerializer(serializers.ModelSerializer):
    """Сериализатор статистики"""
    label = serializers.SerializerMethodField()
    
    class Meta:
        model = ClubStats
        fields = ['id', 'value', 'label', 'icon', 'order']
    
    def get_label(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_label(language)


class ClubPageSerializer(serializers.Serializer):
    """Сериализатор для всей страницы клубов с заголовками и статистикой"""
    title = serializers.CharField()
    subtitle = serializers.CharField()
    stats = ClubStatsSerializer(many=True)
    categories = ClubCategorySerializer(many=True)
    clubs = ClubListSerializer(many=True)

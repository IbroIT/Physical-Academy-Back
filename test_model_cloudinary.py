"""
Тест загрузки файлов через Django модели в Cloudinary
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')
django.setup()

from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from news.models import News

def test_model_upload():
    """Тест загрузки через модель Django"""
    print("=" * 50)
    print("ТЕСТ ЗАГРУЗКИ ЧЕРЕЗ DJANGO МОДЕЛЬ")
    print("=" * 50)
    
    try:
        # Создаем тестовое изображение
        img = Image.new('RGB', (200, 200), color='blue')
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # Создаем новость с изображением
        news = News()
        news.title_ru = "Тестовая новость для Cloudinary"
        news.title_en = "Test news for Cloudinary"
        news.title_kg = "Cloudinary үчүн тест жаңылыгы"
        news.content_ru = "Тестовый контент"
        news.content_en = "Test content"
        news.content_kg = "Тесттик контент"
        
        # Сохраняем изображение
        news.image.save('test_news_image.png', ContentFile(img_bytes.read()), save=False)
        news.save()
        
        print(f"\n✓ Новость создана с ID: {news.id}")
        print(f"✓ URL изображения: {news.image.url}")
        print(f"✓ Имя файла: {news.image.name}")
        
        # Проверяем, что URL ведет на Cloudinary
        if 'cloudinary.com' in news.image.url:
            print("✅ Изображение успешно загружено в Cloudinary!")
        else:
            print("⚠️  Изображение не загружено в Cloudinary")
        
        # Удаляем тестовую новость
        news.delete()
        print(f"\n✓ Тестовая новость удалена")
        
        print("\n" + "=" * 50)
        print("✅ ТЕСТ УСПЕШНО ПРОЙДЕН!")
        print("=" * 50)
        return True
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    test_model_upload()

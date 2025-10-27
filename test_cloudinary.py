"""
Тестовый скрипт для проверки подключения к Cloudinary
"""
import os
import sys

# Очищаем кэш модулей для свежего импорта
if 'django' in sys.modules:
    del sys.modules['django']
if 'django.conf' in sys.modules:
    del sys.modules['django.conf']

from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')

import django
django.setup()

import cloudinary
import cloudinary.uploader
from django.core.files.storage import default_storage
from django.conf import settings

def test_cloudinary_connection():
    """Тест подключения к Cloudinary"""
    print("=" * 50)
    print("ПРОВЕРКА КОНФИГУРАЦИИ CLOUDINARY")
    print("=" * 50)
    
    # Проверяем конфигурацию Django settings
    print(f"\n✓ Django DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}")
    print(f"✓ Django MEDIA_URL: {settings.MEDIA_URL}")
    
    # Проверяем конфигурацию Cloudinary
    print(f"\n✓ Cloudinary Cloud Name: {cloudinary.config().cloud_name}")
    print(f"✓ Cloudinary API Key: {cloudinary.config().api_key}")
    print(f"✓ Cloudinary API Secret: {'*' * len(str(cloudinary.config().api_secret))}")
    
    # Проверяем хранилище Django
    print(f"\n✓ Default Storage Class: {default_storage.__class__.__name__}")
    print(f"✓ Default Storage Module: {default_storage.__class__.__module__}")
    
    # Проверяем, является ли это Cloudinary хранилищем
    is_cloudinary = 'cloudinary' in default_storage.__class__.__module__.lower()
    print(f"✓ Is Cloudinary Storage: {is_cloudinary}")
    
    print("\n" + "=" * 50)
    print("ПРОВЕРКА ЗАГРУЗКИ В CLOUDINARY")
    print("=" * 50)
    
    # Тестовая загрузка (создаем временный текстовый файл)
    try:
        from io import BytesIO
        from PIL import Image
        
        # Создаем простое тестовое изображение
        img = Image.new('RGB', (100, 100), color='red')
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # Загружаем в Cloudinary через Django storage
        file_path = default_storage.save('test/test_image.png', img_bytes)
        print(f"\n✓ Файл успешно загружен: {file_path}")
        
        # Получаем URL
        file_url = default_storage.url(file_path)
        print(f"✓ URL файла: {file_url}")
        
        # Удаляем тестовый файл
        default_storage.delete(file_path)
        print(f"✓ Тестовый файл удален")
        
        print("\n" + "=" * 50)
        print("✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО!")
        print("=" * 50)
        return True
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {str(e)}")
        print("\n" + "=" * 50)
        print("❌ ПРОВЕРКА НЕ ПРОЙДЕНА")
        print("=" * 50)
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    test_cloudinary_connection()

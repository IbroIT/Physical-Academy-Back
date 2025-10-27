"""
Скрипт для миграции существующих медиа-файлов в Cloudinary
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')
django.setup()

from django.core.files import File
from pathlib import Path
import cloudinary.uploader

def migrate_media_files():
    """
    Миграция локальных медиа-файлов в Cloudinary
    
    ВНИМАНИЕ: Запускайте только после создания бэкапа базы данных!
    """
    print("=" * 60)
    print("МИГРАЦИЯ МЕДИА-ФАЙЛОВ В CLOUDINARY")
    print("=" * 60)
    
    # Путь к папке media
    media_root = Path(__file__).resolve().parent / 'media'
    
    if not media_root.exists():
        print("\n⚠️  Папка media/ не найдена. Миграция не требуется.")
        return
    
    print(f"\n📁 Путь к медиа: {media_root}")
    
    # Подсчитываем файлы
    all_files = list(media_root.rglob('*'))
    files_to_migrate = [f for f in all_files if f.is_file()]
    
    print(f"📊 Найдено файлов: {len(files_to_migrate)}")
    
    if not files_to_migrate:
        print("\n✅ Нет файлов для миграции")
        return
    
    # Показываем первые 10 файлов
    print("\n📝 Примеры файлов:")
    for f in files_to_migrate[:10]:
        relative_path = f.relative_to(media_root)
        print(f"   - {relative_path}")
    
    if len(files_to_migrate) > 10:
        print(f"   ... и ещё {len(files_to_migrate) - 10} файлов")
    
    print("\n" + "=" * 60)
    print("⚠️  ВАЖНО!")
    print("=" * 60)
    print("""
Этот скрипт загрузит все файлы из папки media/ в Cloudinary.

Перед запуском миграции:
1. Создайте бэкап базы данных
2. Убедитесь, что Cloudinary настроен правильно
3. Проверьте лимиты вашего плана Cloudinary

Файлы будут загружены с сохранением структуры папок.

ПРИМЕЧАНИЕ: Этот скрипт только загружает файлы в Cloudinary.
Обновление ссылок в БД требует отдельной миграции для каждой модели.
    """)
    
    response = input("\nПродолжить миграцию? (yes/no): ")
    
    if response.lower() != 'yes':
        print("\n❌ Миграция отменена")
        return
    
    print("\n" + "=" * 60)
    print("🚀 НАЧАЛО МИГРАЦИИ")
    print("=" * 60)
    
    success_count = 0
    error_count = 0
    
    for file_path in files_to_migrate:
        relative_path = file_path.relative_to(media_root)
        
        try:
            with open(file_path, 'rb') as f:
                # Загружаем файл в Cloudinary
                result = cloudinary.uploader.upload(
                    f,
                    folder=f"media/{relative_path.parent}",
                    public_id=file_path.stem,
                    resource_type='auto'
                )
                
                print(f"✓ {relative_path} -> {result['secure_url']}")
                success_count += 1
                
        except Exception as e:
            print(f"✗ Ошибка при загрузке {relative_path}: {str(e)}")
            error_count += 1
    
    print("\n" + "=" * 60)
    print("📊 РЕЗУЛЬТАТЫ МИГРАЦИИ")
    print("=" * 60)
    print(f"✅ Успешно загружено: {success_count}")
    print(f"❌ Ошибок: {error_count}")
    print(f"📝 Всего файлов: {len(files_to_migrate)}")
    print("\n⚠️  Не забудьте обновить ссылки в базе данных!")
    print("=" * 60)

if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════╗
║  СКРИПТ МИГРАЦИИ МЕДИА-ФАЙЛОВ В CLOUDINARY                 ║
╚════════════════════════════════════════════════════════════╝

Этот скрипт НЕ запускается автоматически!

Текущий статус:
- ✅ Cloudinary настроен и работает
- ✅ Новые файлы автоматически загружаются в Cloudinary
- ⚠️  Старые файлы из папки media/ остаются локально

Если вам нужно мигрировать существующие файлы:
1. Раскомментируйте строку ниже
2. Запустите скрипт: python migrate_to_cloudinary.py

Для миграции раскомментируйте следующую строку:
""")
    
    # migrate_media_files()  # Раскомментируйте для запуска миграции
    
    print("\n✋ Миграция не запущена (закомментирована)")
    print("Для запуска раскомментируйте вызов migrate_media_files()")

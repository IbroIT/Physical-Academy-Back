# Интеграция Cloudinary для медиа-файлов

## ✅ Что было сделано

### 1. Установлены необходимые пакеты
Пакеты уже были в `requirements.txt`:
- `cloudinary` - основной SDK для работы с Cloudinary
- `django-cloudinary-storage` - Django интеграция для хранения файлов

### 2. Настроены переменные окружения в `.env`
```env
CLOUDINARY_CLOUD_NAME=dyg5p8i69
CLOUDINARY_API_KEY=228724766473381
CLOUDINARY_API_SECRET=rZpe1h81K8nlygwBIgBsb4Kd3ac
```

### 3. Обновлены настройки Django (`ac_back/settings.py`)

#### a) Правильный порядок приложений в `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "cloudinary_storage",  # Должен быть перед django.contrib.staticfiles
    "cloudinary",          # Cloudinary основной пакет
    # ... остальные приложения
]
```

#### b) Конфигурация Cloudinary:
```python
cloudinary.config( 
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET'),
    secure = True
)
```

#### c) Настройка хранилищ (Django 4.2+ формат):
```python
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'  # для обратной совместимости
```

## 📁 Работа с файлами

### Модели не требуют изменений
Все существующие модели с `ImageField` и `FileField` автоматически будут использовать Cloudinary:

```python
class News(models.Model):
    image = models.ImageField(upload_to='news/')  # Автоматически загружается в Cloudinary
```

### Пример использования:
```python
# Создание объекта с файлом
news = News()
news.image.save('photo.jpg', file_content, save=True)

# URL будет указывать на Cloudinary
print(news.image.url)  # https://res.cloudinary.com/dyg5p8i69/image/upload/v1/media/news/photo_xxxxx.jpg
```

## 🧪 Тестирование

Созданы два тестовых скрипта:

1. **`test_cloudinary.py`** - базовая проверка подключения к Cloudinary
2. **`test_model_cloudinary.py`** - проверка загрузки через Django модели

Запуск тестов:
```bash
python test_cloudinary.py
python test_model_cloudinary.py
```

## ✅ Результаты

- ✅ Файлы загружаются напрямую в Cloudinary
- ✅ URL файлов теперь ведут на `https://res.cloudinary.com/...`
- ✅ Автоматическая оптимизация изображений
- ✅ CDN для быстрой загрузки файлов
- ✅ Не нужно хранить медиа-файлы на сервере

## 📝 Важные замечания

1. **Все новые файлы** автоматически загружаются в Cloudinary
2. **Старые файлы** остаются в локальной папке `media/` - их нужно будет мигрировать отдельно если требуется
3. **При деплое на Heroku/Railway** больше не нужно беспокоиться о потере медиа-файлов при рестарте
4. **Статические файлы** (CSS, JS) остаются на обычном хранилище - их можно тоже перенести на Cloudinary при необходимости

## 🚀 Деплой

Для деплоя на Heroku/Railway нужно добавить переменные окружения:
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

После этого приложение будет автоматически использовать Cloudinary для всех медиа-файлов.

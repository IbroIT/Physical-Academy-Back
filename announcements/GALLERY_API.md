# 📸 API Documentation - Announcements Gallery

## Обновленные эндпоинты

### 1. GET `/api/announcements/` - Список объявлений

**Параметры:**

- `lang` (optional): `ru` | `en` | `kg` - язык перевода

**Response:**

```json
{
  "success": true,
  "count": 10,
  "announcements": [
    {
      "id": 1,
      "image_url": "https://example.com/media/announcements/main.jpg",
      "gallery_images": [
        {
          "id": 1,
          "image_url": "https://example.com/media/announcements/gallery/photo1.jpg",
          "order": 1
        },
        {
          "id": 2,
          "image_url": "https://example.com/media/announcements/gallery/photo2.jpg",
          "order": 2
        }
      ],
      "urgency": "high",
      "is_active": true,
      "order": 0,
      "created_at": "2025-11-07T10:00:00Z",
      "title": "Заголовок",
      "description": "Описание",
      "category": "Категория",
      "department": "Отдел",
      "content": "Полное содержание"
    }
  ]
}
```

---

### 2. GET `/api/announcements/{id}/` - Детали объявления

**Параметры:**

- `id` (required): ID объявления
- `lang` (optional): `ru` | `en` | `kg` - язык перевода

**Response:**

```json
{
  "success": true,
  "announcement": {
    "id": 1,
    "image_url": "https://example.com/media/announcements/main.jpg",
    "gallery_images": [
      {
        "id": 1,
        "image_url": "https://example.com/media/announcements/gallery/photo1.jpg",
        "order": 1
      },
      {
        "id": 2,
        "image_url": "https://example.com/media/announcements/gallery/photo2.jpg",
        "order": 2
      },
      {
        "id": 3,
        "image_url": "https://example.com/media/announcements/gallery/photo3.jpg",
        "order": 3
      }
    ],
    "urgency": "high",
    "is_active": true,
    "order": 0,
    "created_at": "2025-11-07T10:00:00Z",
    "title": "Заголовок объявления",
    "description": "Краткое описание",
    "category": "Важное",
    "department": "Деканат",
    "content": "Полное содержание объявления..."
  }
}
```

---

## Изменения в структуре данных

### Новое поле: `gallery_images`

Массив дополнительных изображений для галереи:

```typescript
interface AnnouncementImage {
  id: number; // ID изображения
  image_url: string; // Полный URL изображения
  order: number; // Порядок отображения
}

interface Announcement {
  // ... существующие поля
  gallery_images: AnnouncementImage[]; // НОВОЕ!
}
```

---

## Оптимизация запросов

В `views.py` добавлен `prefetch_related` для оптимизации:

```python
queryset = Announcement.objects.filter(is_active=True).prefetch_related(
    'translations',      # Переводы
    'gallery_images'     # Изображения галереи
)
```

Это уменьшает количество SQL запросов с N+1 до 3 запросов.

---

## Frontend интеграция

### Обработка изображений:

```javascript
// 1. Получаем данные с API
const response = await axios.get(`/api/announcements/${id}/?lang=ru`);
const announcement = response.data.announcement;

// 2. Формируем массив всех изображений
const allImages = [];

// Главное изображение первым
if (announcement.image_url) {
  allImages.push(announcement.image_url);
}

// Добавляем изображения из галереи
if (announcement.gallery_images) {
  announcement.gallery_images.forEach((img) => {
    allImages.push(img.image_url);
  });
}

// 3. Отображаем в галерее
<Gallery images={allImages} />;
```

---

## Примеры использования

### Получить объявление с галереей:

```bash
curl "https://physical-academy-backend.herokuapp.com/api/announcements/1/?lang=ru"
```

### Получить все объявления на английском:

```bash
curl "https://physical-academy-backend.herokuapp.com/api/announcements/?lang=en"
```

---

## Важные замечания

1. **Главное изображение** (`image_url`) всегда одно
2. **Галерея** (`gallery_images`) может содержать 0-N изображений
3. Изображения в галерее **отсортированы** по полю `order`
4. Все URL изображений **абсолютные** (включают домен)
5. API **оптимизирован** через `prefetch_related`

---

## Производительность

### До оптимизации:

- 1 запрос для объявления
- N запросов для переводов
- M запросов для изображений
- **Итого: 1 + N + M запросов** 😱

### После оптимизации:

- 1 запрос для объявлений
- 1 запрос для всех переводов
- 1 запрос для всех изображений
- **Итого: 3 запроса** ✅

---

## Тестирование

После миграций проверьте:

```bash
# 1. Создайте объявление через админку
# 2. Загрузите несколько изображений в галерею
# 3. Проверьте API:

curl "http://localhost:8000/api/announcements/1/?lang=ru"

# Должны увидеть gallery_images в ответе
```

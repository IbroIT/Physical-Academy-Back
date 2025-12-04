# Faculties API Documentation

## Обзор

API для управления данными факультетов. Каждый факультет имеет отдельное приложение с идентичной структурой моделей и API endpoints.

## Структура приложений

- `coaching_faculy` - Тренерский факультет
- `military_faculty` - Военный факультет
- `correspondence_faculty` - Заочный факультет
- `pedagogical_faculty` - Педагогический факультет

## Модели

### TabCategory

Категории/табы для организации контента факультета.

Поля:

- `key` (string) - уникальный ключ категории (history, about, management, specializations, departments)
- `title` (string) - название категории
- `icon_svg` (text) - SVG код иконки
- `order` (int) - порядок отображения
- `is_active` (boolean) - активность

### Card

Карточки с контентом для каждой категории (кроме history).

Поля:

- `tab` (FK) - связь с TabCategory
- `title` (string) - заголовок карточки
- `description` (text) - описание
- `order` (int) - порядок отображения
- `is_active` (boolean) - активность
- `created_at` (datetime) - дата создания
- `updated_at` (datetime) - дата обновления

### TimelineEvent

События для отображения истории факультета (timeline).

Поля:

- `year` (string) - год события
- `event` (text) - описание события
- `order` (int) - порядок отображения
- `is_active` (boolean) - активность
- `created_at` (datetime) - дата создания
- `updated_at` (datetime) - дата обновления

## API Endpoints

### 1. Тренерский факультет

```
GET /api/faculties/coaching/
```

### 2. Военный факультет

```
GET /api/faculties/military/
```

### 3. Заочный факультет

```
GET /api/faculties/correspondence/
```

### 4. Педагогический факультет

```
GET /api/faculties/pedagogical/
```

## Формат ответа

Все endpoints возвращают данные в одинаковом формате:

```json
{
  "tabs": [
    {
      "id": 1,
      "key": "history",
      "title": "История",
      "icon_svg": "<svg>...</svg>",
      "order": 1,
      "cards": []
    },
    {
      "id": 2,
      "key": "about",
      "title": "О факультете",
      "icon_svg": "<svg>...</svg>",
      "order": 2,
      "cards": [
        {
          "id": 1,
          "title": "Миссия",
          "description": "Описание миссии факультета...",
          "order": 1
        },
        {
          "id": 2,
          "title": "Видение",
          "description": "Описание видения факультета...",
          "order": 2
        }
      ]
    }
  ],
  "timeline": [
    {
      "id": 1,
      "year": "1995",
      "event": "Основание факультета",
      "order": 1
    },
    {
      "id": 2,
      "year": "2000",
      "event": "Первый выпуск",
      "order": 2
    }
  ]
}
```

## Примеры использования

### JavaScript/React

```javascript
const fetchFacultyData = async (facultyType) => {
  const response = await fetch(
    `http://localhost:8000/api/faculties/${facultyType}/`
  );
  const data = await response.json();
  return data;
};

// Использование
const coachingData = await fetchFacultyData("coaching");
const militaryData = await fetchFacultyData("military");
```

### Axios

```javascript
import axios from "axios";

const getFacultyData = (facultyType) => {
  return axios
    .get(`/api/faculties/${facultyType}/`)
    .then((response) => response.data);
};

// Использование
getFacultyData("pedagogical").then((data) => {
  console.log(data.tabs);
  console.log(data.timeline);
});
```

## Установка и миграции

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Создать миграции

```bash
python manage.py makemigrations coaching_faculy military_faculty correspondence_faculty pedagogical_faculty
```

### 3. Применить миграции

```bash
python manage.py migrate
```

### 4. Создать суперпользователя (если нужно)

```bash
python manage.py createsuperuser
```

### 5. Запустить сервер

```bash
python manage.py runserver
```

## Админ-панель

Каждый факультет имеет свой раздел в Django Admin:

- **Coaching Faculy** - управление тренерским факультетом
- **Military Faculty** - управление военным факультетом
- **Correspondence Faculty** - управление заочным факультетом
- **Pedagogical Faculty** - управление педагогическим факультетом

В каждом разделе доступны:

- Tab categories (с inline редактированием карточек)
- Cards (отдельное управление карточками)
- Timeline events (управление событиями истории)

## Фильтры и поиск в админке

### TabCategory

- Фильтры: is_active
- Поиск: title, key
- Сортировка: order
- Inline редактирование: Cards

### Card

- Фильтры: tab, is_active, created_at
- Поиск: title, description
- Сортировка: tab, order
- Быстрое редактирование: order, is_active

### TimelineEvent

- Фильтры: is_active, created_at
- Поиск: year, event
- Сортировка: order
- Быстрое редактирование: order, is_active

## Рекомендации по заполнению данных

### Рекомендуемые ключи для TabCategory

- `history` - История факультета (используется с TimelineEvent)
- `about` - О факультете
- `management` - Руководство
- `specializations` - Специализации
- `departments` - Кафедры

### Порядок заполнения

1. Создайте TabCategory для каждой секции
2. Для секции `history` создайте TimelineEvent события
3. Для остальных секций создайте Card карточки
4. Настройте `order` для правильной сортировки
5. Используйте `is_active` для временного скрытия элементов

## CORS настройки

API настроен для работы с фронтендом на localhost. Убедитесь что в settings.py указаны правильные CORS origins:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    # добавьте ваши домены
]
```

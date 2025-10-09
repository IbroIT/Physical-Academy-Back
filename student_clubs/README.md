# Student Clubs Backend

Django REST API для управления студенческими клубами с поддержкой трех языков (ru, en, kg).

## Установка и запуск

### 1. Применить миграции
```bash
python manage.py makemigrations student_clubs
python manage.py migrate
```

### 2. Создать тестовые данные
```bash
python manage.py create_clubs_sample_data
```

### 3. Запустить сервер
```bash
python manage.py runserver
```

### 4. Доступ к API
- API: http://localhost:8000/api/student-clubs/
- Документация: http://localhost:8000/api/docs/
- Admin: http://localhost:8000/admin/

## Быстрый старт

### Основные эндпоинты:

1. **Получить все данные страницы** (рекомендуется для фронтенда):
   ```
   GET /api/student-clubs/clubs/page_data/?lang=ru
   ```

2. **Список клубов с фильтрацией**:
   ```
   GET /api/student-clubs/clubs/?lang=ru&category=tech&search=python
   ```

3. **Детали клуба**:
   ```
   GET /api/student-clubs/clubs/1/?lang=en
   ```

4. **Присоединиться к клубу**:
   ```
   POST /api/student-clubs/clubs/1/join/
   Body: {"email": "user@example.com", "name": "John Doe"}
   ```

## Особенности

✅ **Поддержка 3 языков**: ru, en, kg  
✅ **Фильтрация по категориям**: ?category=tech  
✅ **Поиск**: ?search=programming  
✅ **Цели и мотивация**: вместо событий и расписания  
✅ **Ссылка для присоединения**: join_link поле  
✅ **Руководители клубов**: вложенные данные  
✅ **Статистика**: общая информация о клубах  
✅ **Django Admin**: полная поддержка редактирования  

## Структура приложения

```
student_clubs/
├── models.py              # 4 модели: Club, ClubCategory, ClubLeader, ClubStats
├── serializers.py         # Сериализаторы с поддержкой языков
├── views.py               # ViewSets с фильтрацией
├── urls.py                # API маршруты
├── admin.py               # Админ-панель
├── management/
│   └── commands/
│       └── create_clubs_sample_data.py  # Команда для тестовых данных
└── API_DOCUMENTATION.md   # Полная документация API
```

## Модели

### Club (Клуб)
Основная модель с мультиязычными полями:
- Название, описание (краткое и полное)
- Цели и мотивация
- Расписание встреч
- Категория, статус, иконка
- Количество участников
- Ссылка для присоединения
- Теги для поиска

### ClubCategory (Категория)
Категории клубов: tech, sports, arts, science, social, business

### ClubLeader (Руководитель)
Информация о руководителях клубов с контактами

### ClubStats (Статистика)
Общая статистика для отображения на странице

## Примеры использования в React

```javascript
// Получить все данные страницы
const data = await fetch('/api/student-clubs/clubs/page_data/?lang=ru')
  .then(res => res.json());

// Фильтрация по категории
const techClubs = await fetch('/api/student-clubs/clubs/?category=tech&lang=en')
  .then(res => res.json());

// Присоединиться к клубу
const result = await fetch('/api/student-clubs/clubs/1/join/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: 'user@example.com', name: 'John' })
}).then(res => res.json());
```

## Полная документация

См. файл [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) для подробной документации всех эндпоинтов.

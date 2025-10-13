# 🎓 API Документация: Студенты и Членство в клубах

## 📋 Основные эндпоинты

### 1. Список студентов

```http
GET /api/student-clubs/students/?lang=ru&search=Иванов&faculty=IT
```

**Параметры запроса:**

- `lang` - язык (ru, en, kg)
- `search` - поиск по имени/email/факультету
- `faculty` - фильтрация по факультету
- `year_of_study` - фильтрация по курсу (1-6)
- `interests` - фильтрация по интересам (через запятую)

**Пример ответа:**

```json
{
  "count": 10,
  "next": "http://localhost:8000/api/student-clubs/students/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "full_name": "Иванов Иван Иванович",
      "email": "ivanov@example.com",
      "faculty": "Факультет информационных технологий",
      "year_of_study": 3,
      "photo": "http://localhost:8000/media/student_profiles/ivanov.jpg"
    },
    {
      "id": 2,
      "full_name": "Петров Петр Петрович",
      "email": "petrov@example.com",
      "faculty": "Факультет информационных технологий",
      "year_of_study": 2,
      "photo": null
    }
  ]
}
```

### 2. Детали профиля студента

```http
GET /api/student-clubs/students/1/?lang=en
```

**Пример ответа:**

```json
{
  "id": 1,
  "full_name": "Ivan Ivanov",
  "email": "ivanov@example.com",
  "phone": "+996 555 123456",
  "faculty": "Faculty of Information Technology",
  "year_of_study": 3,
  "major": "Software Engineering",
  "bio": "I am a third-year student interested in web development",
  "interests": ["programming", "design", "gaming"],
  "photo": "http://localhost:8000/media/student_profiles/ivanov.jpg",
  "is_active": true,
  "created_at": "2023-06-15T14:30:00Z",
  "updated_at": "2023-06-16T10:15:30Z"
}
```

### 3. Создание профиля студента

```http
POST /api/student-clubs/students/
```

**Тело запроса:**

```json
{
  "full_name_ru": "Новый Студент",
  "full_name_en": "New Student",
  "full_name_kg": "Жаңы Студент",
  "email": "new.student@example.com",
  "phone": "+996 555 111222",
  "faculty_ru": "Экономический факультет",
  "faculty_en": "Faculty of Economics",
  "faculty_kg": "Экономика факультети",
  "year_of_study": 1,
  "major_ru": "Финансы и кредит",
  "major_en": "Finance and Credit",
  "major_kg": "Финансы жана насыя",
  "interests": ["economics", "finance", "analytics"]
}
```

### 4. Клубы студента

```http
GET /api/student-clubs/students/1/my_clubs/?lang=ru
```

**Пример ответа:**

```json
{
  "id": 1,
  "full_name_ru": "Иванов Иван Иванович",
  "email": "ivanov@example.com",
  "memberships": [
    {
      "id": 1,
      "status": "approved",
      "joined_at": "2023-06-15T15:30:00Z",
      "club": {
        "id": 1,
        "name": "IT Club",
        "icon": "💻",
        "category": {
          "id": 1,
          "name": "Технологии"
        }
      }
    },
    {
      "id": 2,
      "status": "pending",
      "joined_at": "2023-06-16T10:00:00Z",
      "club": {
        "id": 2,
        "name": "Дебатный клуб",
        "icon": "🎯",
        "category": {
          "id": 3,
          "name": "Социальные"
        }
      }
    }
  ]
}
```

### 5. Список членств в клубах

```http
GET /api/student-clubs/memberships/?club=1&status=approved&lang=ru
```

**Параметры запроса:**

- `club` - ID клуба
- `student` - ID студента
- `status` - фильтрация по статусу (pending, approved, leader, rejected, left)
- `lang` - язык (ru, en, kg)

**Пример ответа:**

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "student": {
        "id": 1,
        "full_name": "Иванов Иван Иванович",
        "email": "ivanov@example.com",
        "faculty": "Факультет информационных технологий",
        "year_of_study": 3,
        "photo": "http://localhost:8000/media/student_profiles/ivanov.jpg"
      },
      "club": {
        "id": 1,
        "name": "IT Club",
        "category": {
          "id": 1,
          "name": "Технологии",
          "slug": "tech"
        },
        "icon": "💻"
      },
      "status": "approved",
      "joined_at": "2023-06-15T15:30:00Z",
      "role": "Активный участник"
    }
  ]
}
```

### 6. Члены клуба

```http
GET /api/student-clubs/memberships/club_members/?club=1&status=approved&lang=en
```

**Параметры запроса:**

- `club` - ID клуба (обязательный)
- `status` - статус членства (по умолчанию "approved")
- `lang` - язык (ru, en, kg)

**Пример ответа:**

```json
[
  {
    "id": 1,
    "student": {
      "id": 1,
      "full_name": "Ivan Ivanov",
      "email": "ivanov@example.com",
      "faculty": "Faculty of Information Technology",
      "year_of_study": 3,
      "photo": "http://localhost:8000/media/student_profiles/ivanov.jpg"
    },
    "club": {
      "id": 1,
      "name": "IT Club",
      "icon": "💻"
    },
    "status": "approved",
    "joined_at": "2023-06-15T15:30:00Z",
    "role": "Active Member"
  }
]
```

### 7. Присоединение к клубу

```http
POST /api/student-clubs/memberships/join_club/
```

**Тело запроса:**

```json
{
  "student": 1,
  "club": 2,
  "motivation_text": "Хочу вступить в клуб для развития навыков публичных выступлений"
}
```

**Пример ответа:**

```json
{
  "success": true,
  "message": "Заявка на вступление отправлена",
  "membership_id": 3,
  "status": "pending"
}
```

### 8. Обновление статуса членства

```http
POST /api/student-clubs/memberships/3/update_status/
```

**Тело запроса:**

```json
{
  "status": "approved"
}
```

**Пример ответа:**

```json
{
  "success": true,
  "message": "Статус обновлен на Участник",
  "status": "approved"
}
```

---

## 🚀 Инструкция по использованию API

### Получение списка студентов

```javascript
// Получить всех студентов
const students = await fetch("/api/student-clubs/students/?lang=ru").then(
  (res) => res.json()
);

// Поиск по имени
const foundStudents = await fetch(
  "/api/student-clubs/students/?search=Иванов&lang=ru"
).then((res) => res.json());

// Фильтрация по факультету и курсу
const filteredStudents = await fetch(
  "/api/student-clubs/students/?faculty=IT&year_of_study=3&lang=ru"
).then((res) => res.json());
```

### Получение клубов студента

```javascript
// Получить все клубы конкретного студента
const studentClubs = await fetch(
  "/api/student-clubs/students/1/my_clubs/?lang=ru"
).then((res) => res.json());
```

### Получение членов клуба

```javascript
// Получить всех участников клуба
const members = await fetch(
  "/api/student-clubs/memberships/club_members/?club=1&lang=ru"
).then((res) => res.json());

// Получить лидеров клуба
const leaders = await fetch(
  "/api/student-clubs/memberships/club_members/?club=1&status=leader&lang=ru"
).then((res) => res.json());
```

### Присоединение к клубу

```javascript
// Отправить заявку на вступление в клуб
const result = await fetch("/api/student-clubs/memberships/join_club/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    student: 1,
    club: 2,
    motivation_text: "Хочу развить навыки программирования",
  }),
}).then((res) => res.json());
```

---

## 📊 Модели данных

### StudentProfile (Профиль студента)

- **Основная информация:**

  - ФИО на 3 языках (full_name_ru, full_name_en, full_name_kg)
  - Email, телефон
  - Фото профиля

- **Учебная информация:**
  - Факультет на 3 языках (faculty_ru, faculty_en, faculty_kg)
  - Курс обучения (year_of_study)
  - Специальность на 3 языках (major_ru, major_en, major_kg)
- **Дополнительно:**
  - Биография на 3 языках (bio_ru, bio_en, bio_kg)
  - Интересы (JSON массив)
  - Флаг активности (is_active)
  - Даты создания/обновления

### ClubMembership (Членство в клубах)

- **Основная информация:**
  - Студент (FK → StudentProfile)
  - Клуб (FK → Club)
  - Статус (pending/approved/leader/rejected/left)
  - Даты присоединения и обновления
- **Дополнительно:**
  - Мотивация для вступления (text)
  - Роль в клубе на 3 языках (role_ru, role_en, role_kg)

---

## 🔄 Статусы членства

- **pending** - Заявка на рассмотрении
- **approved** - Участник клуба
- **leader** - Руководитель/Заместитель
- **rejected** - Заявка отклонена
- **left** - Покинул клуб

---

## 🛠️ Дополнительные возможности

### Создание тестовых данных

```bash
python manage.py create_students_sample_data
```

Команда создаст:

- 20 студенческих профилей с разными факультетами и курсами
- 30-60 членств в клубах с разными статусами

---

## 📝 Примечания

1. **Автоматическое обновление счетчика участников:**
   При создании нового членства или изменении статуса существующего автоматически обновляется счетчик участников в модели Club.

2. **Уникальность членства:**
   Один студент может иметь только одно членство в конкретном клубе. При повторной попытке вступления в тот же клуб будет возвращена ошибка.

3. **Поддержка языков:**
   Все текстовые поля поддерживают 3 языка (ru, en, kg). Используйте параметр `lang=` для получения данных на нужном языке.

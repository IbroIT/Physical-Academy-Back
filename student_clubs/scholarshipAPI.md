# API Documentation: Стипендии и Визовая поддержка

## Общая информация

API предоставляет доступ к данным о стипендиальных программах и визовой поддержке для студентов.
Для всех эндпоинтов можно указать язык ответа через параметр запроса `lang` (допустимые значения: `ru`, `en`, `kg`).

## Стипендиальные программы

### Получение списка стипендиальных программ

**URL:** `/api/students/scholarship/programs/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:**

```json
[
  {
    "id": 1,
    "name": "Президентская стипендия",
    "description": "Стипендия для особо отличившихся студентов",
    "eligibility_criteria": "Средний балл не менее 4.8, активное участие в жизни университета",
    "amount": "10000.00",
    "currency": "KGS",
    "application_deadline": "2023-09-01",
    "application_link": "https://example.com/apply",
    "contact_email": "scholarship@example.com",
    "contact_phone": "+996 XXX XXX XXX",
    "required_documents": [
      {
        "id": 1,
        "name": "Заявление",
        "description": "Форма заявления на получение стипендии",
        "is_required": true,
        "order": 1
      },
      {
        "id": 2,
        "name": "Транскрипт",
        "description": "Выписка из зачетной книжки",
        "is_required": true,
        "order": 2
      }
    ],
    "is_active": true
  }
]
```

### Получение деталей стипендиальной программы

**URL:** `/api/students/scholarship/programs/{id}/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:** Аналогичен списку, но для одной программы.

### Получение списка требуемых документов

**URL:** `/api/students/scholarship/documents/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)
- `scholarship_id` - ID стипендиальной программы для фильтрации (опционально)

**Пример ответа:**

```json
[
  {
    "id": 1,
    "name": "Заявление",
    "description": "Форма заявления на получение стипендии",
    "is_required": true,
    "order": 1
  }
]
```

### Получение всех данных для страницы стипендий

**URL:** `/api/students/scholarship/page_data/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:**

```json
{
  "scholarships": [
    {
      "id": 1,
      "name": "Президентская стипендия",
      "description": "Стипендия для особо отличившихся студентов",
      "eligibility_criteria": "Средний балл не менее 4.8, активное участие в жизни университета",
      "amount": "10000.00",
      "currency": "KGS",
      "application_deadline": "2023-09-01",
      "application_link": "https://example.com/apply",
      "contact_email": "scholarship@example.com",
      "contact_phone": "+996 XXX XXX XXX",
      "required_documents": [
        {
          "id": 1,
          "name": "Заявление",
          "description": "Форма заявления на получение стипендии",
          "is_required": true,
          "order": 1
        }
      ],
      "is_active": true
    }
  ],
  "total_scholarships": 5,
  "active_scholarships": 3
}
```

## Визовая поддержка

### Получение списка сервисов визовой поддержки

**URL:** `/api/students/visa-support/services/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:**

```json
[
  {
    "id": 1,
    "title": "Консультация по визовым вопросам",
    "description": "Индивидуальные консультации для иностранных студентов",
    "is_featured": true,
    "icon": "fa-passport",
    "order": 1,
    "is_active": true
  }
]
```

### Получение выделенных сервисов визовой поддержки

**URL:** `/api/students/visa-support/services/featured/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:** Аналогичен списку сервисов, но содержит только выделенные.

### Получение списка контактов визовой поддержки

**URL:** `/api/students/visa-support/contacts/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:**

```json
[
  {
    "id": 1,
    "full_name": "Иванов Иван Иванович",
    "position": "Специалист по визовой поддержке",
    "email": "visa@example.com",
    "phone": "+996 XXX XXX XXX",
    "photo": "/media/visa_support/ivanov.jpg",
    "office_location": "Главный корпус, кабинет 123",
    "office_hours": "Пн-Пт, 9:00-17:00",
    "order": 1,
    "is_active": true
  }
]
```

### Получение всех данных для страницы визовой поддержки

**URL:** `/api/students/visa-support/page_data/`

**Метод:** `GET`

**Параметры запроса:**

- `lang` - язык ответа (опционально, по умолчанию `ru`)

**Пример ответа:**

```json
{
  "services": [
    {
      "id": 1,
      "title": "Консультация по визовым вопросам",
      "description": "Индивидуальные консультации для иностранных студентов",
      "is_featured": true,
      "icon": "fa-passport",
      "order": 1,
      "is_active": true
    }
  ],
  "contacts": [
    {
      "id": 1,
      "full_name": "Иванов Иван Иванович",
      "position": "Специалист по визовой поддержке",
      "email": "visa@example.com",
      "phone": "+996 XXX XXX XXX",
      "photo": "/media/visa_support/ivanov.jpg",
      "office_location": "Главный корпус, кабинет 123",
      "office_hours": "Пн-Пт, 9:00-17:00",
      "order": 1,
      "is_active": true
    }
  ],
  "featured_services": [
    {
      "id": 1,
      "title": "Консультация по визовым вопросам",
      "description": "Индивидуальные консультации для иностранных студентов",
      "is_featured": true,
      "icon": "fa-passport",
      "order": 1,
      "is_active": true
    }
  ]
}
```

## Интеграция с Frontend

Для интеграции с frontend-компонентами следует использовать соответствующие API-эндпоинты:

1. Для страницы стипендий: `/api/students/scholarship/page_data/`
2. Для страницы визовой поддержки: `/api/students/visa-support/page_data/`

Оба эндпоинта поддерживают параметр `lang` для локализации контента.

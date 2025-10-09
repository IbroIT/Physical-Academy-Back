# Leadership Structure API Documentation

This API provides comprehensive endpoints for managing and retrieving leadership and administrative structure data with full support for 3 languages (Russian, Kyrgyz, English).

## Base URL
```
/api/leadership-structure/
```

## Authentication
Currently, all endpoints are read-only and don't require authentication.

## Language Support
All endpoints support 3 languages: **Russian (ru)**, **Kyrgyz (kg)**, and **English (en)**.

### Language Selection Methods:

1. **Query Parameter** (Recommended):
   ```
   GET /api/leadership-structure/board-of-trustees/?lang=kg
   GET /api/leadership-structure/board-of-trustees/?lang=en
   GET /api/leadership-structure/board-of-trustees/?lang=ru
   ```

2. **Accept-Language Header**:
   ```
   Accept-Language: ky
   Accept-Language: en
   Accept-Language: ru
   ```

**Default Language**: Russian (ru) if no language is specified.

---

## Endpoints Overview

### 1. Board of Trustees (Попечительский совет)

#### 1.1 List All Trustees
```http
GET /api/leadership-structure/board-of-trustees/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `search` (optional): Search by name or position
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Иванов Иван Иванович",
    "name_kg": "Иванов Иван Ивановичтин аты",
    "name_en": "Ivanov Ivan Ivanovich",
    "position": "Председатель попечительского совета",
    "position_kg": "Камкорчулук кеңешинин төрагасы",
    "position_en": "Chairman of the Board of Trustees",
    "bio": "Опытный руководитель с 20-летним стажем...",
    "bio_kg": "20 жылдык тажрыйбасы бар...",
    "bio_en": "Experienced leader with 20 years...",
    "achievements": [
      "Награжден орденом...",
      "Автор более 50 публикаций...",
      "Руководитель проекта..."
    ],
    "achievements_kg": [
      "Орден менен сыйланган...",
      "50дөн ашык басылмалардын автору...",
      "Долбоордун жетекчиси..."
    ],
    "achievements_en": [
      "Awarded with order...",
      "Author of over 50 publications...",
      "Project leader..."
    ],
    "email": "ivanov@academy.ru",
    "phone": "+7 (495) 123-45-67",
    "image": "/media/trustees/ivanov.jpg",
    "image_url": "http://example.com/media/trustees/ivanov.jpg",
    "icon": "👑",
    "order": 1
  }
]
```

#### 1.2 Get Single Trustee
```http
GET /api/leadership-structure/board-of-trustees/{id}/
```

**Response:** Same as list item above.

#### 1.3 Board of Trustees Statistics
```http
GET /api/leadership-structure/board-of-trustees-stats/
```

**Response Example:**
```json
[
  {
    "id": 1,
    "label": "Лет опыта",
    "label_kg": "Тажрыйба жылдары",
    "label_en": "Years of experience",
    "target_value": 25,
    "icon": "📅",
    "color": "from-blue-500 to-blue-600",
    "order": 1
  },
  {
    "id": 2,
    "label": "Реализованных проектов",
    "label_kg": "Ишке ашырылган долбоорлор",
    "label_en": "Completed projects",
    "target_value": 150,
    "icon": "🚀",
    "color": "from-green-500 to-green-600",
    "order": 2
  }
]
```

---

### 2. Audit Commission (Ревизионная комиссия)

#### 2.1 List All Commission Members
```http
GET /api/leadership-structure/audit-commission/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `search` (optional): Search by name, position, or department
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Петров Петр Петрович",
    "name_kg": "Петров Петр Петровичтин аты",
    "name_en": "Petrov Petr Petrovich",
    "position": "Председатель комиссии",
    "position_kg": "Комиссиянын төрагасы",
    "position_en": "Chairman of the Commission",
    "department": "Финансовый отдел",
    "department_kg": "Финансы бөлүмү",
    "department_en": "Finance Department",
    "achievements": [
      "Проведение финансовых аудитов",
      "Контроль бюджета",
      "Анализ расходов"
    ],
    "achievements_kg": [
      "Финансылык аудиттерди өткөрүү",
      "Бюджетти көзөмөлдөө",
      "Чыгымдарды талдоо"
    ],
    "achievements_en": [
      "Conducting financial audits",
      "Budget control",
      "Expense analysis"
    ],
    "email": "petrov@academy.ru",
    "phone": "+7 (495) 123-45-68",
    "image": "/media/audit_commission/petrov.jpg",
    "image_url": "http://example.com/media/audit_commission/petrov.jpg",
    "order": 1
  }
]
```

#### 2.2 Get Single Commission Member
```http
GET /api/leadership-structure/audit-commission/{id}/
```

#### 2.3 Audit Commission Statistics
```http
GET /api/leadership-structure/audit-commission-statistics/
```

**Response Example:**
```json
[
  {
    "id": 1,
    "label": "Проверок в год",
    "label_kg": "Жылына текшерүүлөр",
    "label_en": "Annual audits",
    "value": "50+",
    "value_kg": "50+",
    "value_en": "50+",
    "icon": "📊",
    "order": 1
  }
]
```

---

### 3. Academic Council (Ученый совет)

#### 3.1 List All Council Members
```http
GET /api/leadership-structure/academic-council/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `search` (optional): Search by name, position, or department
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Сидорова Анна Владимировна",
    "name_kg": "Сидорова Анна Владимировнанын аты",
    "name_en": "Sidorova Anna Vladimirovna",
    "position": "Председатель ученого совета",
    "position_kg": "Окумуштуулар кеңешинин төрагасы",
    "position_en": "Chairman of the Academic Council",
    "department": "Кафедра физической культуры",
    "department_kg": "Дене тарбия кафедрасы",
    "department_en": "Department of Physical Culture",
    "achievements": [
      "Доктор педагогических наук",
      "Автор 100+ научных работ",
      "Лауреат премии"
    ],
    "achievements_kg": [
      "Педагогикалык илимдердин доктору",
      "100+ илимий эмгектердин автору",
      "Сыйлыктын лауреаты"
    ],
    "achievements_en": [
      "Doctor of Pedagogical Sciences",
      "Author of 100+ scientific works",
      "Award laureate"
    ],
    "email": "sidorova@academy.ru",
    "phone": "+7 (495) 123-45-69",
    "image": "/media/academic_council/sidorova.jpg",
    "image_url": "http://example.com/media/academic_council/sidorova.jpg",
    "order": 1
  }
]
```

#### 3.2 Get Single Council Member
```http
GET /api/leadership-structure/academic-council/{id}/
```

---

### 4. Trade Union (Профсоюз)

#### 4.1 Trade Union Benefits
```http
GET /api/leadership-structure/trade-union/benefits/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `ordering` (optional): Sort by order or title

**Response Example:**
```json
[
  {
    "id": 1,
    "title": "Социальная защита",
    "title_kg": "Социалдык коргоо",
    "title_en": "Social Protection",
    "description": "Полная социальная поддержка всех членов профсоюза",
    "description_kg": "Профсоюздун бардык мүчөлөрүнө толук социалдык колдоо",
    "description_en": "Full social support for all union members",
    "icon": "🛡️",
    "order": 1
  },
  {
    "id": 2,
    "title": "Льготы и компенсации",
    "title_kg": "Жеңилдиктер жана компенсациялар",
    "title_en": "Benefits and Compensations",
    "description": "Дополнительные выплаты и компенсации",
    "description_kg": "Кошумча төлөмдөр жана компенсациялар",
    "description_en": "Additional payments and compensations",
    "icon": "💰",
    "order": 2
  }
]
```

#### 4.2 Trade Union Events
```http
GET /api/leadership-structure/trade-union/events/
```

**Response Example:**
```json
[
  {
    "id": 1,
    "title": "Новогодний праздник",
    "title_kg": "Жаңы жыл майрамы",
    "title_en": "New Year Celebration",
    "date": "31 декабря 2024",
    "date_kg": "2024-жылдын 31-декабры",
    "date_en": "December 31, 2024",
    "description": "Праздничное мероприятие для всех членов",
    "description_kg": "Бардык мүчөлөр үчүн майрамдык иш-чара",
    "description_en": "Festive event for all members",
    "image": "/media/trade_union_events/newyear.jpg",
    "image_url": "http://example.com/media/trade_union_events/newyear.jpg",
    "icon": "🎉",
    "order": 1
  }
]
```

#### 4.3 Trade Union Statistics
```http
GET /api/leadership-structure/trade-union/stats/
```

**Response Example:**
```json
[
  {
    "id": 1,
    "label": "Членов профсоюза",
    "label_kg": "Профсоюз мүчөлөрү",
    "label_en": "Union Members",
    "value": 250,
    "icon": "👥",
    "color": "from-blue-500 to-green-500",
    "order": 1
  },
  {
    "id": 2,
    "label": "Лет работы",
    "label_kg": "Иштөө жылдары",
    "label_en": "Years of operation",
    "value": 15,
    "icon": "📅",
    "color": "from-green-500 to-blue-500",
    "order": 2
  }
]
```

---

### 5. Commissions (Комиссии)

#### 5.1 List All Commissions
```http
GET /api/leadership-structure/commissions/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `category` (optional): Filter by category (academic, quality, student, methodical, all)
- `search` (optional): Search by name or chairman
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Методическая комиссия",
    "name_kg": "Методикалык комиссия",
    "name_en": "Methodological Commission",
    "chairman": "Кузнецов Алексей Петрович",
    "chairman_kg": "Кузнецов Алексей Петрович",
    "chairman_en": "Kuznetsov Alexey Petrovich",
    "description": "Разработка учебно-методических материалов",
    "description_kg": "Окуу-методикалык материалдарды иштеп чыгуу",
    "description_en": "Development of educational materials",
    "members": [
      "Иванов И.И.",
      "Петров П.П.",
      "Сидорова А.В."
    ],
    "members_kg": [
      "Иванов И.И.",
      "Петров П.П.",
      "Сидорова А.В."
    ],
    "members_en": [
      "Ivanov I.I.",
      "Petrov P.P.",
      "Sidorova A.V."
    ],
    "responsibilities": [
      "Разработка программ",
      "Методическая поддержка",
      "Контроль качества"
    ],
    "responsibilities_kg": [
      "Программаларды иштеп чыгуу",
      "Методикалык колдоо",
      "Сапатты көзөмөлдөө"
    ],
    "responsibilities_en": [
      "Program development",
      "Methodological support",
      "Quality control"
    ],
    "category": "methodical",
    "category_display": "Методические",
    "icon": "📋",
    "email": "commission@academy.ru",
    "phone": "+7 (495) 123-45-70",
    "order": 1
  }
]
```

#### 5.2 Get Single Commission
```http
GET /api/leadership-structure/commissions/{id}/
```

#### 5.3 Get Commissions by Category
```http
GET /api/leadership-structure/commissions/by_category/?category=academic
```

**Available Categories:**
- `academic` - Академические
- `quality` - Качество образования
- `student` - Студенческие
- `methodical` - Методические
- `all` - Все

---

### 6. Administrative Structure

#### 6.1 Administrative Departments
```http
GET /api/leadership-structure/administrative/departments/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `search` (optional): Search by name or head
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Ректорат",
    "name_kg": "Ректорат",
    "name_en": "Rectorate",
    "head": "Иванов Иван Иванович",
    "head_kg": "Иванов Иван Иванович",
    "head_en": "Ivanov Ivan Ivanovich",
    "responsibilities": [
      "Общее руководство академией",
      "Стратегическое планирование",
      "Координация подразделений",
      "Внешние связи"
    ],
    "responsibilities_kg": [
      "Академияны жалпы башкаруу",
      "Стратегиялык пландаштыруу",
      "Бөлүмдөрдү координациялоо",
      "Тышкы байланыштар"
    ],
    "responsibilities_en": [
      "General management of the academy",
      "Strategic planning",
      "Coordination of departments",
      "External relations"
    ],
    "email": "rectorat@academy.ru",
    "phone": "+7 (495) 123-45-67",
    "icon": "🏛️",
    "order": 1
  },
  {
    "id": 2,
    "name": "Учебный отдел",
    "name_kg": "Окуу бөлүмү",
    "name_en": "Academic Department",
    "head": "Петрова Мария Сергеевна",
    "head_kg": "Петрова Мария Сергеевна",
    "head_en": "Petrova Maria Sergeevna",
    "responsibilities": [
      "Организация учебного процесса",
      "Контроль успеваемости",
      "Расписание занятий",
      "Аттестация студентов"
    ],
    "responsibilities_kg": [
      "Окуу процессин уюштуруу",
      "Үлгөрүмдү көзөмөлдөө",
      "Сабактардын графиги",
      "Студенттерди аттестациялоо"
    ],
    "responsibilities_en": [
      "Organization of educational process",
      "Performance monitoring",
      "Class schedule",
      "Student certification"
    ],
    "email": "academic@academy.ru",
    "phone": "+7 (495) 123-45-68",
    "icon": "📚",
    "order": 2
  }
]
```

#### 6.2 Get Single Department
```http
GET /api/leadership-structure/administrative/departments/{id}/
```

---

#### 6.3 Administrative Units
```http
GET /api/leadership-structure/administrative/units/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)
- `search` (optional): Search by name, description, or head
- `ordering` (optional): Sort by fields (order, name, created_at)

**Response Example:**
```json
[
  {
    "id": 1,
    "name": "Ректорат",
    "name_kg": "Ректорат",
    "name_en": "Rectorate",
    "description": "Высший орган управления академией",
    "description_kg": "Академиянын эң жогорку башкаруу органы",
    "description_en": "Supreme governing body of the academy",
    "head": "Иванов Иван Иванович",
    "head_kg": "Иванов Иван Иванович",
    "head_en": "Ivanov Ivan Ivanovich",
    "location": "Главное здание, 1 этаж",
    "location_kg": "Башкы имарат, 1-кабат",
    "location_en": "Main building, 1st floor",
    "staff": "15 сотрудников",
    "staff_kg": "15 кызматкер",
    "staff_en": "15 employees",
    "responsibilities": [
      "Общее руководство",
      "Стратегическое планирование",
      "Координация деятельности"
    ],
    "responsibilities_kg": [
      "Жалпы башкаруу",
      "Стратегиялык пландаштыруу",
      "Ишти координациялоо"
    ],
    "responsibilities_en": [
      "General management",
      "Strategic planning",
      "Activity coordination"
    ],
    "email": "rector@academy.ru",
    "phone": "+7 (495) 111-11-11",
    "icon": "🏛️",
    "color": "blue",
    "color_class": "from-blue-500 to-blue-600",
    "order": 1
  },
  {
    "id": 2,
    "name": "Учебный отдел",
    "name_kg": "Окуу бөлүмү",
    "name_en": "Academic Department",
    "description": "Организация и контроль учебного процесса",
    "description_kg": "Окуу процессин уюштуруу жана көзөмөлдөө",
    "description_en": "Organization and control of educational process",
    "head": "Петрова Мария Сергеевна",
    "head_kg": "Петрова Мария Сергеевна",
    "head_en": "Petrova Maria Sergeevna",
    "location": "Главное здание, 2 этаж, каб. 201",
    "location_kg": "Башкы имарат, 2-кабат, 201-бөлмө",
    "location_en": "Main building, 2nd floor, room 201",
    "staff": "10 сотрудников",
    "staff_kg": "10 кызматкер",
    "staff_en": "10 employees",
    "responsibilities": [
      "Составление расписания",
      "Контроль успеваемости",
      "Организация экзаменов"
    ],
    "responsibilities_kg": [
      "Графикти түзүү",
      "Үлгөрүмдү көзөмөлдөө",
      "Экзамендерди уюштуруу"
    ],
    "responsibilities_en": [
      "Schedule compilation",
      "Performance monitoring",
      "Exam organization"
    ],
    "email": "education@academy.ru",
    "phone": "+7 (495) 111-22-22",
    "icon": "📚",
    "color": "green",
    "color_class": "from-green-500 to-green-600",
    "order": 2
  }
]
```

#### 6.4 Get Single Unit
```http
GET /api/leadership-structure/administrative/units/{id}/
```

---

## Common Response Fields

### Multilingual Fields
All text fields are available in 3 languages:
- `field` - Russian (default)
- `field_kg` - Kyrgyz
- `field_en` - English

The API automatically returns the appropriate language based on the `lang` parameter or `Accept-Language` header.

### System Fields
All models include:
- `id` - Unique identifier
- `order` - Display order
- `is_active` - Active status (only active items are returned)
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

### Image Fields
- `image` - Relative URL to the image file
- `image_url` - Absolute URL to the image (includes domain)

---

## Error Responses

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 400 Bad Request
```json
{
  "field_name": [
    "Error message"
  ]
}
```

---

## Pagination

By default, all list endpoints return all items. If pagination is needed in the future, it can be configured in Django REST Framework settings.

---

## Filtering and Searching

### Search
Use the `search` query parameter to search across multiple fields:
```
GET /api/leadership-structure/board-of-trustees/?search=Иванов
```

### Ordering
Use the `ordering` query parameter to sort results:
```
GET /api/leadership-structure/board-of-trustees/?ordering=order
GET /api/leadership-structure/board-of-trustees/?ordering=-created_at
```

Use `-` prefix for descending order.

---

## Examples

### Example 1: Get Board of Trustees in Kyrgyz
```bash
curl -X GET "http://localhost:8000/api/leadership-structure/board-of-trustees/?lang=kg"
```

### Example 2: Get Academic Council in English
```bash
curl -X GET "http://localhost:8000/api/leadership-structure/academic-council/?lang=en"
```

### Example 3: Filter Commissions by Category
```bash
curl -X GET "http://localhost:8000/api/leadership-structure/commissions/?category=academic&lang=ru"
```

### Example 4: Search Administrative Units
```bash
curl -X GET "http://localhost:8000/api/leadership-structure/administrative/units/?search=Ректорат&lang=kg"
```

---

## Integration with Frontend

### React/JavaScript Example

```javascript
// Using fetch API
const fetchBoardOfTrustees = async (lang = 'ru') => {
  const response = await fetch(
    `http://localhost:8000/api/leadership-structure/board-of-trustees/?lang=${lang}`
  );
  const data = await response.json();
  return data;
};

// Usage
const trustees = await fetchBoardOfTrustees('en');
console.log(trustees);
```

### Using with i18n
```javascript
import { useTranslation } from 'react-i18next';

function BoardOfTrusteesComponent() {
  const { i18n } = useTranslation();
  const [trustees, setTrustees] = useState([]);
  
  useEffect(() => {
    const lang = i18n.language === 'ky' ? 'kg' : i18n.language;
    fetch(`/api/leadership-structure/board-of-trustees/?lang=${lang}`)
      .then(res => res.json())
      .then(data => setTrustees(data));
  }, [i18n.language]);
  
  return (
    <div>
      {trustees.map(trustee => (
        <div key={trustee.id}>
          <h3>{trustee.name}</h3>
          <p>{trustee.position}</p>
          <p>{trustee.bio}</p>
        </div>
      ))}
    </div>
  );
}
```

---

## Notes

1. **Language Fallback**: If a translation is not available for the requested language, the API falls back to Russian (ru).

2. **JSON Fields**: Fields like `achievements`, `members`, and `responsibilities` are stored as JSON arrays and support multilingual content.

3. **Image URLs**: Images are served from the `/media/` directory. Make sure to configure `MEDIA_URL` and `MEDIA_ROOT` in Django settings.

4. **Read-Only**: All endpoints are currently read-only. For content management, use the Django Admin panel.

5. **Category Values**: Commission categories are:
   - `academic` - Академические
   - `quality` - Качество образования  
   - `student` - Студенческие
   - `methodical` - Методические
   - `all` - Все

---

## Support

For issues or questions, please contact the development team or refer to the main API documentation.

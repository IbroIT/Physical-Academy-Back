# Universal Education Pages API Documentation

## Overview

Universal API для страниц факультетов и отделений с полной поддержкой локализации (RU, EN, KG).

## Модели

### EducationPage

Главная модель для страниц факультетов и отделений.

**Поля:**

- `slug` - уникальный URL идентификатор (например: `coaching-faculty`, `general-departments`)
- `page_type` - тип страницы (выбор из предопределенных типов)
- `title_ru`, `title_en`, `title_kg` - заголовок на трёх языках
- `description_ru`, `description_en`, `description_kg` - описание на трёх языках
- `banner_image` - баннер страницы
- `is_active` - активна ли страница
- `order` - порядок сортировки

### EducationSection

Разделы внутри страницы.

**Поля:**

- `page` - связь с EducationPage
- `title_ru`, `title_en`, `title_kg` - заголовок раздела на трёх языках
- `order` - порядок сортировки

### EducationItem

Элементы внутри раздела.

**Поля:**

- `section` - связь с EducationSection
- `text_ru`, `text_en`, `text_kg` - текст элемента на трёх языках
- `order` - порядок сортировки

## API Endpoints

### 1. Получить страницу факультета

```
GET /api/education/faculties/<slug>/?lang=<language>
```

**Параметры:**

- `slug` - идентификатор страницы (например: `coaching-faculty`)
- `lang` - язык (ru|en|kg, по умолчанию: ru)

**Примеры:**

```bash
# Русский язык (по умолчанию)
GET /api/education/faculties/coaching-faculty/

# Английский язык
GET /api/education/faculties/coaching-faculty/?lang=en

# Киргизский язык
GET /api/education/faculties/coaching-faculty/?lang=kg
```

**Ответ:**

```json
{
  "title": "Факультет тренерского мастерства",
  "banner_image": "/media/education_pages/banner.jpg",
  "description": "Подготовка высококвалифицированных тренеров...",
  "sections": [
    {
      "section_title": "Программы обучения",
      "items": [
        "Бакалавриат по тренерскому делу",
        "Магистратура по спортивной педагогике",
        "Докторантура по теории физической культуры"
      ]
    },
    {
      "section_title": "Специализации",
      "items": ["Футбол", "Баскетбол", "Легкая атлетика"]
    }
  ]
}
```

### 2. Получить страницу отделения

```
GET /api/education/departments/<slug>/?lang=<language>
```

**Параметры:**

- `slug` - идентификатор страницы (например: `general-departments`)
- `lang` - язык (ru|en|kg, по умолчанию: ru)

**Примеры:**

```bash
# Русский язык
GET /api/education/departments/general-departments/?lang=ru

# Английский язык
GET /api/education/departments/general-departments/?lang=en
```

**Ответ:** Аналогичен ответу для факультетов.

## Доступные типы страниц (page_type)

```python
PAGE_TYPE_CHOICES = [
    ('coaching_faculty', 'Coaching Faculty'),
    ('correspondence_training', 'Correspondence Training'),
    ('doctorate_program', 'Doctorate Program'),
    ('master_program', 'Master Program'),
    ('military_training', 'Military Training'),
    ('pedagogical_sports', 'Pedagogical Sports'),
    ('general_departments', 'General Departments'),
]
```

## Примеры использования в админке

### Создание новой страницы факультета:

1. **Основная информация:**

   - Slug: `coaching-faculty`
   - Page Type: `Coaching Faculty`
   - Is Active: ✓

2. **Заголовки:**

   - Title (RU): `Факультет тренерского мастерства`
   - Title (EN): `Coaching Faculty`
   - Title (KG): `Машыктыруучулук факультети`

3. **Описания:**

   - Description (RU): `Подготовка высококвалифицированных тренеров...`
   - Description (EN): `Training of highly qualified coaches...`
   - Description (KG): `Жогорку квалификациялуу машыктыруучуларды даярдоо...`

4. **Разделы (через inline):**
   - Добавьте разделы с локализованными заголовками
   - Для каждого раздела добавьте элементы с локализованным текстом

## Преимущества архитектуры

✅ **DRY принцип** - одна модель для всех страниц факультетов/отделений  
✅ **Полная локализация** - все поля на 3 языках (RU, EN, KG)  
✅ **Гибкость** - легко добавлять новые страницы без изменения кода  
✅ **Удобная админка** - inline редактирование разделов и элементов  
✅ **Производительность** - prefetch_related для оптимизации запросов  
✅ **Чистый API** - возвращает только строки, а не объекты {ru, en, kg}

## Миграция данных

После создания миграций (`python manage.py makemigrations education`), примените их:

```bash
python manage.py migrate education
```

## Тестирование API

```bash
# С помощью curl
curl "http://localhost:8000/api/education/faculties/coaching-faculty/?lang=ru"

# С помощью httpie
http GET "http://localhost:8000/api/education/faculties/coaching-faculty/?lang=en"

# С помощью PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/api/education/faculties/coaching-faculty/?lang=kg"
```

## Интеграция с фронтендом

### React компонент (пример):

```javascript
import { useParams } from "react-router-dom";
import { useLanguage } from "@/hooks/useLanguage";

const EducationPage = () => {
  const { slug } = useParams(); // coaching-faculty, master-program и т.д.
  const { lang } = useLanguage(); // ru, en, kg
  const [data, setData] = useState(null);

  useEffect(() => {
    // Автоматически определяет faculties или departments по slug
    const category = slug.includes("departments") ? "departments" : "faculties";

    fetch(`/api/education/${category}/${slug}/?lang=${lang}`)
      .then((res) => res.json())
      .then(setData);
  }, [slug, lang]);

  if (!data) return <Loader />;

  return (
    <div>
      <h1>{data.title}</h1>
      <img src={data.banner_image} alt={data.title} />
      <p>{data.description}</p>

      {data.sections.map((section, idx) => (
        <div key={idx}>
          <h2>{section.section_title}</h2>
          <ul>
            {section.items.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};
```

## Исправления KY → KG

Все упоминания `KY` заменены на `KG` во всех моделях:

- `name_kg` (вместо `name_ky`)
- `description_kg` (вместо `description_ky`)
- `features_kg` (вместо `features_ky`)
- И т.д.

## Поддержка

Для вопросов и предложений обращайтесь к разработчикам проекта.

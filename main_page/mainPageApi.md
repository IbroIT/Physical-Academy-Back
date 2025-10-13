### 1. Статистика для страницы academy/about

```http
api/about/about-statistics
```


```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "titleInt": "1500+",
            "description": "студентов",
            "emoji": "🎓"
        }
    ]
}
```

### 1.1 фото для страницы academy/about 

```http
/api/about/about-photos
```

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "photo": "http://localhost:8000/media/about_photos/Screenshot_From_2025-10-02_20-06-29.png",
            "description": "спортзал"
        }
    ]
}
```

### 2 api для роута academy/history

```http 
api/academy/history-steps/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "year": 2005,
            "title": "Основание академии",
            "description": "Создание академии как центра подготовки специалистов в области физической культуры и спорта. Начало формирования образовательных программ и научной базы.",
            "buildings": 3,
            "students": 500,
            "programs": 12,
            "achievements": [
                "ачылыш"
            ]
        }
    ]
}
```

### 2.1 important dates(важные вехи)
```http
/api/academy/important-dates/
```

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "year": 2008,
            "titleInt": "1000",
            "description": "первые выпускники"
        }
    ]
}
```
### 3 api для academy/mission

```http
/api/academy/missions/
```

```json

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "category": {
                "id": 1,
                "name": "миссия"
            },
            "title": "Наша Миссия",
            "description": "Развивать физическую культуру и спортивную науку через качественное образование, инновационные исследования и подготовку лидеров, способных изменить мир спорта и здорового образа жизни."
        },
        {
            "id": 2,
            "category": {
                "id": 2,
                "name": "видение"
            },
            "title": "Наше Видение",
            "description": "Стать мировым лидером в области спортивного образования, где каждый студент раскрывает свой потенциал, а научные открытия формируют будущее физической культуры и здоровья человечества"
        }
    ]
}
```


### 4. акредитации

```http
api/academy/accreditations/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "accreditation_type": {
                "id": 1,
                "name": "междуранодный"
            },
            "organization": "Organization ru:",
            "validity": "до 2025",
            "description": "Description ru:",
            "photo": "http://localhost:8000/media/accreditation_photos/Screenshot_From_2025-10-10_08-30-32.png",
            "logo": "http://localhost:8000/media/accreditation_logos/Screenshot_From_2025-09-29_08-17-01.png",
            "certificate_number": "48123487102"
        }
    ]
}
```

### 5 достижение для роутинга academy/numbers
```http
api/academy/achievements/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Лучшая спортивная академия",
            "description": "Описание на русском",
            "year": 2025
        }
    ]
}
```

### 5.1 статистика для academy/numbers
```http
api/academy/statistics/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "студентов",
            "description": "усторились на работу",
            "titleInt": "1500+"
        }
    ]
}
```


### 5.2 инфраструка для academy/numbers

```http
api/academy/infrastructure/
```

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "titleInt": "100",
            "description": "спортивные залы",
            "emoji": "🏟️"
        }
    ]
}
```

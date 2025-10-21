### 1 master-programs endpoint

```http
/api/education/master-programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "emoji": "🏃‍♂️",
            "name": "Название (RU):",
            "description": "Описание (RU):",
            "features": [
                "Управление спортивными проектами"
            ],
            "duration_years": 3,
            "offline": true,
            "tuition_fee": "250000.00"
        }
    ]
}
```

### 2 faculties endpoind
```http
/api/education/faculties/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Факультет педагогики и спорта",
            "description": "Описание (RU):",
            "mission": [
                "Преимущество 1"
            ],
            "achievements": [
                "Достижения (RU):"
            ],
            "statistics": [
                {
                    "id": 1,
                    "meaning": "студентов",
                    "titleInt": "10000+"
                }
            ],
            "programs": [
                {
                    "id": 1,
                    "emoji": "🎓",
                    "name": "Название (RU):",
                    "degree": "Бакалавриат",
                    "description": "Описание (RU):",
                    "duration_years": 5,
                    "offline": true,
                    "tuition_fee": "200000.00"
                }
            ],
            "specializations": [
                {
                    "id": 1,
                    "name": "👨‍🏫 Спортивная педагогика",
                    "description": "методики обучения и воспитания в спортивной деятельности",
                    "features": [
                        "Методика тренировок"
                    ]
                }
            ],
            "sports": [
                {
                    "id": 1,
                    "emoji": "⚽",
                    "name": "футбол",
                    "description": "Описание (RU):"
                }
            ],
            "teachers": [
                {
                    "id": 1,
                    "photo": "http://localhost:8000/media/faculty_teachers/Screenshot_From_2025-10-10_09-31-03.png",
                    "full_name": "Полное имя (RU):",
                    "position": "Должность (RU):"
                }
            ],
            "contacts": [
                {
                    "id": 1,
                    "title": "Заголовок (RU):",
                    "value": "077772127398704981"
                }
            ]
        }
    ]
}

```


### 3. college programs endpoint

```http
api/education/college-programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "emoji": "🔰",
            "name": "Название (RU):🔰",
            "description": "Описание (RU):",
            "features": [
                "Особенности (RU):"
            ],
            "duration_years": 4,
            "offline": true,
            "tuition_fee": "2222222.00"
        }
    ]
}
```

### phd programs endpoint

```http
api/education/phd-programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "emoji": "🔰",
            "name": "Название (RU):🔰",
            "description": "Описание (RU):",
            "features": [
                "Особенности (RU):"
            ],
            "duration_years": 4,
            "offline": true,
            "tuition_fee": "2222222.00"
        }
    ]
}
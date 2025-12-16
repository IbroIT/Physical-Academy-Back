## универсальная документация для всех факультетов
## название Faculty
## везде где написанно coaching заменить наподходящий факультет (military,coaching,correspondence,pedagogical)
### название Faculty Management Api

```http
/api/faculties/coaching/management/ 
```

```json
    {
        "id": 1,
        "name": "AKTAN KASHYMBEKOV",
        "role": "афуцафцу",
        "photo": "https://res.cloudinary.com/dyg5p8i69/image/upload/v1765861417/syc2ndjoxika129iqr5m.pdf",
        "phone": "55555",
        "email": "aktam200e@gmail.com",
        "resume": "https://res.cloudinary.com/dyg5p8i69/raw/upload/v1765861418/owqmzghtytt97w3innkw.jpg",
        "order": 0
    }
```

### Coaching Faculty Specializations Api

```http
/api/faculties/coaching/specializations/
```

```json
    {
        "id": 1,
        "title": "Название (EN):",
        "description": "fasefadsf",
        "order": 0
    }
```
### Coaching Faculty Departments Api не использовать для correspondence и military
```http
/api/faculties/coaching/departments/
```

```json
    {
        "id": 1,
        "name": "Название (RU):",
        "description": "фыуваыфвафыа",
        "staff": [
            {
                "id": 1,
                "name": "bdfy",
                "position": "adsasdasdasd",
                "resume": "https://res.cloudinary.com/dyg5p8i69/raw/upload/v1765861332/sitevowntm9sjdhhchru.jpg",
                "order": 0
            }
        ],
        "order": 0
    }
```
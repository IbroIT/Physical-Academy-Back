## coaching faculty

### to get all tabs 
```http
/api/faculties/coaching/tabs/
```

```json 
[
    {
        "id": 1,
        "key": "history",
        "title": "история",
        "icon": "📚",
        "order": 0
    },
    {
        "id": 2,
        "key": "coaching",
        "title": "Заголовок (Русский):",
        "icon": "эмодзи",
        "order": 0
    }
]
```

### cards

```http
/api/faculties/coaching/cards/?tab=coaching 
<!-- Это пример -->
<!-- вместо  coaching key который указали в tabs-->
```
```json
[
    {
        "id": 1,
        "title": "Заголовок (Русский):",
        "description": "Русский",
        "order": 0
    }
]
```

### to get history
```http
/api/faculties/coaching/history/
```
```json
[
    {
        "id": 2,
        "year": "2123",
        "event": "Событие (Русский):",
        "order": 0
    }
]
```

### to get about us

```http
/api/faculties/coaching/about/?lang=kg
```
```json
[
    {
        "id": 1,
        "text": "awfeawefawdf",
        "order": 0
    },
    {
        "id": 2,
        "text": "awfeawefawdf",
        "order": 0
    }
]
```
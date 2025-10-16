
All endpoints support 3 languages: **Russian (ru)**, **Kyrgyz (kg)**, and **English (en)**.

1. **Query Parameter** (Recommended):
   ```
   GET /api/admission/aspirant-documents/?lang=kg
   GET /api/admission/aspirant-documents/?lang=ru
   GET /api/admission/aspirant-documents/?lang=en
   ```

2. **Accept-Language Header**:
   ```
   Accept-Language: ky
   Accept-Language: en
   Accept-Language: ru
   ```

**Default Language**: Russian (ru) if no language is specified.


## Endpoints Overview

### 1. Aspirant- documents 

#### 1.1 List All documents
```http
GET /api/admission/aspirant-documents/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)

**response example**

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "document_name": "PhD admission rules",
            "order": 1,
            "file": "http://localhost:8000/media/aspirant_documents/aspirant_doc_1.txt"
        },
    ]
}
```

### 2. Aspirant-programs 

#### 1.1 List All programs
```http
GET /api/admission/aspirant-programs/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)

**response example**

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "program_name": "Theory and methodology of physical education, sports training, health and adaptive physical culture",
            "description": "Training highly qualified scientific personnel in the field of theory and methodology of physical education and sports.",
            "order": 1,
            "features": [
                "Scientific research in sports",
                "Innovative training methods",
                "Interdisciplinary approach",
                "Publications in international journals"
            ]
        },
    ]
}
```

### 3. Aspirant-main-dates

#### 1.1 List All main-dates
```http
GET /api/admission/aspirant-main-dates/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)

**response example**

```json


{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "event_name": "Document submission",
            "date": "1 мая - 30 июня",
            "order": 1
        },
    ]
}
```

### 4. Aspirant-requirements

#### 1.1 List All requirements
```http
GET /api/admission/aspirant-requirements/
```

**Query Parameters:**
- `lang` (optional): Language code (ru, kg, en)

**response example**

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "description": "Master's or specialist diploma in a relevant specialty. Average grade not less than 4.0.",
            "order": 1,
            "title": "Education"
        },
    ]
}
```



### 5. the same thing above goes with api endpoints like:


```http
GET /api/admission/master-requirements/
GET /api/admission/master-main-dates/
GET /api/admission/master-programs/
GET /api/admission/master-documents/
```

**каждый из них дает данные про магистр. там используются те же поля что в endpoints for aspirant**




### 6. api for doctor's degree section


```http
GET /api/admission/doctor-admission-steps/
GET /api/admission/doctor-statistics/
GET /api/admission/doctor-programs/
```

### 6.1 

```http
/api/admission/doctor-admission-steps/?lang=en
```

```json 
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "apply documents",
            "description": "prepare and apply documents",
            "deadline": "20 august",
            "requirement": "documents"
        }
    ]
}
```

### 6.2 

```http
/api/admission/doctor-statistics/?lang=en
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "titleInt": "70%",
            "description": "guard works"
        }
    ]
}
```

### 6.3
```http
GET /api/admission/doctor-programs/?lang=en
```

```json
[
    {
        "id": 1,
        "program_name": "programm",
        "duration": 5,
        "features": [
            "bio"
        ],
        "short_description": "Short Description (English):"
    }
]
```

### 6.4 
```http
GET /api/admission/doctor-programs/?lang=en&id=1
```

```json
{
    "id": 1,
    "program_name": "programm",
    "description": "Description (English):",
    "features": [
        "bio"
    ],
    "duration": 5
}
```

### 7 college api -- college programs
programs

```http
GET /api/admission/doctor-programs/?lang=en&id=1
```

```json
{
    "id": 1,
    "program_name": "Program Name(kyrgyz):",
    "description": "Description (кыргыз):",
    "features": [
        "биомеханика"
    ],
    "duration": 3
}
```

### 7.1  college admission requirements

```http
api/admission/college-admission-requirements/
```

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "подать заявку",
            "description": "подать заявку туда сюда",
            "duration": "до 20 августа"
        }
    ]
}
```

### 7.2 college admission steps
```http 
api/admission/college-admission-steps/

```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "подать заявку",
            "description": "подать заявку туда сюда",
            "duration": "до 20 августа"
        }
    ]
}
```

### 7.3 college statistics

```http
api/admission/college-statistics/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "titleInt": "1500+",
            "description": "студенты"
        }
    ]
}
```

### 7.4 college soon events
```http
api/admission/college-soon-events/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "event": "подача заявок"
        }
    ]
}
```



### 8. bachelor quatas endpoints


### 8.1
```http
api/admission/quata-types/
```
```json
[
        {
            "id": 1,
            "type": "sports",
            "title": "одаренным",
            "description": "Description (Russian):",
            "icon": "emoji",
            "spots": 9,
            "deadline": "10",
            "color": "blue",
            "order": 1,
            "requirements": [
                {
                    "id": 1,
                    "requirement": "Requirement (Russian):",
                    "order": 1
                }
            ],
            "benefits": [
                {
                    "id": 1,
                    "benefit": "Benefit (Russian)",
                    "order": 0
                }
            ]
        }
]
```



### 8.2.api/admission/quota-stats

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "stat_type": "total_spots",
            "number": "8798",
            "label": "Benefit (English)",
            "description": "Description (Russian):",
            "order": 2
        }
    ]
}
```

### 8.3.api/admission/additional-support
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "support": "Support (Russian):",
            "order": 1
        }
    ]
}
```
### 8.4.api/admission/process-steps
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "step_number": 1,
            "title": "Title (Russian):",
            "description": "Description (Russian):",
            "color_scheme": "from-blue-500 to-cyan-500"
        }
    ]
}
```
### 8.5.api/admission/bachelor-quotas
```json

{
    "quotas": [
        {
            "id": 1,
            "type": "sports",
            "title": "одаренным",
            "description": "Description (Russian):",
            "icon": "emoji",
            "spots": 9,
            "deadline": "10",
            "color": "blue",
            "order": 1,
            "requirements": [
                {
                    "id": 1,
                    "requirement": "Requirement (Russian):",
                    "order": 1
                }
            ],
            "benefits": [
                {
                    "id": 1,
                    "benefit": "Benefit (Russian)",
                    "order": 0
                }
            ]
        }
    ],
    "quota_stats": [
        {
            "id": 1,
            "stat_type": "total_spots",
            "number": "8798",
            "label": "Benefit (English)",
            "description": "Description (Russian):",
            "order": 2
        }
    ],
    "additional_support": [
        {
            "id": 1,
            "support": "Support (Russian):",
            "order": 1
        }
    ],
    "process_steps": [
        {
            "id": 1,
            "step_number": 1,
            "title": "Title (Russian):",
            "description": "Description (Russian):",
            "color_scheme": "from-blue-500 to-cyan-500"
        }
    ]
}
```


### 9 bachelor programs endpoint
```http
api/admission/bachelor-programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Название программы (русский):",
            "description": "Описание программы (русский):",
            "duration": 4,
            "CareerPerspectives": [
                "трудоустроиство"
            ],
            "mainDiscipline": [
                "программы",
                "туда сюда"
            ],
            "Offline": true,
            "emoji": "🎓"
        }
    ]
}
```
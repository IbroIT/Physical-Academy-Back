## disabilities

### 1 Disability Support Service List
```http
/api/student-clubs/disabilities/services/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "🌟",
            "title": "text",
            "description": "text",
            "features": [
                "text"
            ]
        }
    ]
}
```


### 2 Disability Contact Person List
```http
/api/student-clubs/disabilities/contacts/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "👤",
            "name": "Aktan",
            "position": "text",
            "phone": "55555",
            "email": "aktam200e@gmail.com",
            "hours": "text",
            "location": "text"
        }
    ]
}
```
### 3 Disability Resource List

```http
/api/student-clubs/disabilities/resources/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "📚",
            "name": "text",
            "description": "text",
            "url": "http://127.0.0.1:8000/admin/student_clubs/socialnetworkaccount/add/",
            "type": "tool",
            "format": "website"
        }
    ]
}
```
### 4 Disability Emergency Contact List
```http
/api/student-clubs/disabilities/emergency/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "text",
            "description": "text",
            "phone": "55555",
            "phone_link": "text",
            "phoneLink": "text"
        }
    ]
}
```

## Council

### 1 Council Member List
```http
/api/student-clubs/council/members/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "avatar": null,
            "name": "text",
            "role": "member",
            "role_display": "Member",
            "position": "text",
            "department": "text",
            "email": "text@gmail.com",
            "phone": "text",
            "instagram": "http://127.0.0.1:8000/admin/student_clubs/councilmember/add/",
            "linkedin": "http://127.0.0.1:8000/admin/student_clubs/councilmember/add/",
            "bio": "text",
            "achievements": "text"
        }
    ]
}
```


### 2 Council Initiative List
```http
/api/student-clubs/council/initiatives/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "🚀",
            "title": "text",
            "description": "text",
            "goals": "text",
            "status": "in_progress",
            "status_display": "In Progress",
            "start_date": "2025-10-15",
            "end_date": "2025-10-15",
            "lead_members": []
        }
    ]
}
```

### 3 Council Event List
```http
/api/student-clubs/council/events/
```
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "icon": "📅",
            "title": "text",
            "description": "text",
            "status": "ongoing",
            "status_display": "Ongoing",
            "date": "2025-10-15T16:00:37Z",
            "location": "text",
            "registration_link": "http://127.0.0.1:8000/admin/student_clubs/councilevent/add/",
            "image": null,
            "initiative": {
                "id": 1,
                "icon": "🚀",
                "title": "text",
                "description": "text",
                "goals": "text",
                "status": "in_progress",
                "status_display": "In Progress",
                "start_date": "2025-10-15",
                "end_date": "2025-10-15",
                "lead_members": []
            }
        },
        {
            "id": 2,
            "icon": "📅",
            "title": "text",
            "description": "text",
            "status": "past",
            "status_display": "Past",
            "date": "2025-10-15T12:28:21Z",
            "location": "text",
            "registration_link": "http://127.0.0.1:8000/admin/student_clubs/councilevent/add/",
            "image": null,
            "initiative": {
                "id": 1,
                "icon": "🚀",
                "title": "text",
                "description": "text",
                "goals": "text",
                "status": "in_progress",
                "status_display": "In Progress",
                "start_date": "2025-10-15",
                "end_date": "2025-10-15",
                "lead_members": []
            }
        }
    ]
}
```
### 4 Council Stats List
```http
/api/student-clubs/council/stats/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "key": "text",
            "value": "text",
            "label": "text"
        }
    ]
}
```

### 5 Council Page Data List

```http
/api/student-clubs/council-page/
```

```json
{
    "members": [
        {
            "id": 1,
            "avatar": null,
            "name": "text",
            "role": "member",
            "role_display": "Member",
            "position": "text",
            "department": "text",
            "email": "text@gmail.com",
            "phone": "text",
            "instagram": "http://127.0.0.1:8000/admin/student_clubs/councilmember/add/",
            "linkedin": "http://127.0.0.1:8000/admin/student_clubs/councilmember/add/",
            "bio": "text",
            "achievements": "text"
        }
    ],
    "initiatives": [
        {
            "id": 1,
            "icon": "🚀",
            "title": "text",
            "description": "text",
            "goals": "text",
            "status": "in_progress",
            "status_display": "In Progress",
            "start_date": "2025-10-15",
            "end_date": "2025-10-15",
            "lead_members": []
        }
    ],
    "events": [
        {
            "id": 3,
            "icon": "📅",
            "title": "text",
            "description": "text",
            "status": "ongoing",
            "status_display": "Ongoing",
            "date": "2025-10-15T16:00:37Z",
            "location": "text",
            "registration_link": "http://127.0.0.1:8000/admin/student_clubs/councilevent/add/",
            "image": null,
            "initiative": {
                "id": 1,
                "icon": "🚀",
                "title": "text",
                "description": "text",
                "goals": "text",
                "status": "in_progress",
                "status_display": "In Progress",
                "start_date": "2025-10-15",
                "end_date": "2025-10-15",
                "lead_members": []
            }
        },
        {
            "id": 2,
            "icon": "📅",
            "title": "text",
            "description": "text",
            "status": "past",
            "status_display": "Past",
            "date": "2025-10-15T12:28:21Z",
            "location": "text",
            "registration_link": "http://127.0.0.1:8000/admin/student_clubs/councilevent/add/",
            "image": null,
            "initiative": {
                "id": 1,
                "icon": "🚀",
                "title": "text",
                "description": "text",
                "goals": "text",
                "status": "in_progress",
                "status_display": "In Progress",
                "start_date": "2025-10-15",
                "end_date": "2025-10-15",
                "lead_members": []
            }
        }
    ],
    "stats": [
        {
            "key": "text",
            "value": "text",
            "label": "text"
        }
    ]
}
```

## Scholarship 
### 1 Scholarship Required Document List

```http
/api/student-clubs/scholarship/documents/
```

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Транскрипт",
            "description": "Официальный транскрипт с оценками",
            "is_required": true,
            "order": 1
        }
    ]
}
```

### 2 Scholarship Program List
```http
/api/student-clubs/scholarship/programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Стипендия для отличников",
            "description": "Стипендия для студентов с высокой успеваемостью",
            "eligibility_criteria": "GPA 4.0 и выше\nАктивное участие",
            "amount": "5000.00",
            "currency": "KGS",
            "application_deadline": "2025-12-31",
            "application_link": "https://example.com/apply",
            "contact_email": "scholarship@example.com",
            "contact_phone": "+996123456789",
            "required_documents": [
                {
                    "id": 1,
                    "name": "Транскрипт",
                    "description": "Официальный транскрипт с оценками",
                    "is_required": true,
                    "order": 1
                }
            ],
            "is_active": true
        }
    ]
}
```
### 3 Scholarship Page Data List
```http
/api/student-clubs/scholarship-page/
```
```json

{
    "scholarships": [
        {
            "id": 1,
            "name": "Стипендия для отличников",
            "description": "Стипендия для студентов с высокой успеваемостью",
            "eligibility_criteria": "GPA 4.0 и выше\nАктивное участие",
            "amount": "5000.00",
            "currency": "KGS",
            "application_deadline": "2025-12-31",
            "application_link": "https://example.com/apply",
            "contact_email": "scholarship@example.com",
            "contact_phone": "+996123456789",
            "required_documents": [
                {
                    "id": 1,
                    "name": "Транскрипт",
                    "description": "Официальный транскрипт с оценками",
                    "is_required": true,
                    "order": 1
                }
            ],
            "is_active": true
        }
    ],
    "total_scholarships": 1,
    "active_scholarships": 1
}
```
## Visa

### 1 Visa Support Service List
```http
/api/student-clubs/visa/services/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "text",
            "description": "text",
            "is_featured": false,
            "icon": "text",
            "order": 1,
            "is_active": true
        }
    ]
}
```

### 2 Visa Support Contact List
```http
/api/student-clubs/visa/contacts/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "full_name": "text",
            "position": "text",
            "email": "text@gmail.com",
            "phone": "text",
            "photo": null,
            "office_location": "text",
            "office_hours": "text",
            "order": 1,
            "is_active": true
        }
    ]
}
```
## exchange

### 1 Exchange Region List
```http
/api/student-clubs/exchange/regions/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name_ru": "text",
            "name_en": "text",
            "name_kg": "text",
            "code": "text"
        }
    ]
}
```
### 2 Exchange Duration Type List
```http
 /api/student-clubs/exchange/durations/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name_ru": "text",
            "name_en": "text",
            "name_kg": "text",
            "code": "text"
        }
    ]
}
```
### 3 Exchange Program List
```http
/api/student-clubs/exchange/programs/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "university_ru": "text",
            "university_en": "text",
            "university_kg": "text",
            "country_ru": "text",
            "country_en": "text",
            "country_kg": "text",
            "region": 1,
            "region_name": "text",
            "duration_type": 1,
            "duration_type_name": "text",
            "duration_ru": "text",
            "duration_en": "text",
            "duration_kg": "text",
            "description_ru": "text",
            "description_en": "text",
            "description_kg": "text",
            "cost": "text",
            "language_ru": "text",
            "language_en": "text",
            "language_kg": "text",
            "grants_available_ru": "text",
            "grants_available_en": "text",
            "grants_available_kg": "text",
            "deadline": "text",
            "available_spots": 0,
            "icon": "🎓",
            "website": "http://127.0.0.1:8000/admin/student_clubs/exchangeprogram/add/",
            "difficulty": "high",
            "difficulty_label_ru": "text",
            "difficulty_label_en": "text",
            "difficulty_label_kg": "text",
            "is_featured": false,
            "is_active": true,
            "order": 0,
            "requirements": [
                {
                    "id": 1,
                    "text_ru": "text",
                    "text_en": "text",
                    "text_kg": "text",
                    "order": 0
                }
            ],
            "benefits": [
                {
                    "id": 1,
                    "text_ru": "text",
                    "text_en": "text",
                    "text_kg": "text",
                    "order": 0
                }
            ],
            "available_courses": [
                {
                    "id": 1,
                    "name_ru": "text",
                    "name_en": "text",
                    "name_kg": "text"
                }
            ]
        }
    ]
}
```
### 4 Exchange Program Requirement List
```http
/api/student-clubs/exchange/requirements/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "text_ru": "text",
            "text_en": "text",
            "text_kg": "text",
            "order": 0
        }
    ]
}
```
### 5 Exchange Program Benefit List
```http
/api/student-clubs/exchange/benefits/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "text_ru": "text",
            "text_en": "text",
            "text_kg": "text",
            "order": 0
        }
    ]
}
```
### 6 Exchange Program Course List
```http
/api/student-clubs/exchange/courses/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name_ru": "text",
            "name_en": "text",
            "name_kg": "text"
        }
    ]
}
```
### 7 Exchange Page Stat List
```http
/api/student-clubs/exchange/stats/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "🌍",
            "value_ru": "text",
            "value_en": "text",
            "value_kg": "text",
            "label_ru": "text",
            "label_en": "text",
            "label_kg": "text",
            "order": 0
        }
    ]
}
```
### 8 Exchange Deadline List
```http
/api/student-clubs/exchange/deadlines/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "date": "2025-10-15",
            "program_ru": "text",
            "program_en": "text",
            "program_kg": "text",
            "days_left_ru": "text",
            "days_left_en": "text",
            "days_left_kg": "text",
            "order": 0
        }
    ]
}
```

### 8 Exchange Page Data List
```http
/api/student-clubs/exchange-page/
```
```json
{
    "title": "International Exchange Programs",
    "subtitle": "Expand your horizons with our partner universities worldwide and gain invaluable international experience",
    "stats": [
        {
            "id": 1,
            "icon": "🌍",
            "value_ru": "text",
            "value_en": "text",
            "value_kg": "text",
            "label_ru": "text",
            "label_en": "text",
            "label_kg": "text",
            "order": 0
        }
    ],
    "programs": [
        {
            "id": 1,
            "university_ru": "text",
            "university_en": "text",
            "university_kg": "text",
            "country_ru": "text",
            "country_en": "text",
            "country_kg": "text",
            "region": 1,
            "region_name": "text",
            "duration_type": 1,
            "duration_type_name": "text",
            "duration_ru": "text",
            "duration_en": "text",
            "duration_kg": "text",
            "description_ru": "text",
            "description_en": "text",
            "description_kg": "text",
            "cost": "text",
            "language_ru": "text",
            "language_en": "text",
            "language_kg": "text",
            "grants_available_ru": "text",
            "grants_available_en": "text",
            "grants_available_kg": "text",
            "deadline": "text",
            "available_spots": 0,
            "icon": "🎓",
            "website": "http://127.0.0.1:8000/admin/student_clubs/exchangeprogram/add/",
            "difficulty": "high",
            "difficulty_label_ru": "text",
            "difficulty_label_en": "text",
            "difficulty_label_kg": "text",
            "is_featured": false,
            "is_active": true,
            "order": 0,
            "requirements": [
                {
                    "id": 1,
                    "text_ru": "text",
                    "text_en": "text",
                    "text_kg": "text",
                    "order": 0
                }
            ],
            "benefits": [
                {
                    "id": 1,
                    "text_ru": "text",
                    "text_en": "text",
                    "text_kg": "text",
                    "order": 0
                }
            ],
            "available_courses": [
                {
                    "id": 1,
                    "name_ru": "text",
                    "name_en": "text",
                    "name_kg": "text"
                }
            ]
        }
    ],
    "filters": {
        "regions": [
            {
                "id": 1,
                "name": "text",
                "code": "text"
            }
        ],
        "durations": [
            {
                "id": 1,
                "name": "text",
                "code": "text"
            }
        ]
    },
    "deadlines": {
        "title": "Upcoming Deadlines",
        "list": [
            {
                "id": 1,
                "date": "2025-10-15",
                "program_ru": "text",
                "program_en": "text",
                "program_kg": "text",
                "days_left_ru": "text",
                "days_left_en": "text",
                "days_left_kg": "text",
                "order": 0
            }
        ]
    }
}
```

## Instruction 
### 1 Instruction Category List
```http
/api/student-clubs/instructions/categories/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name_ru": "text",
            "name_en": "text",
            "name_kg": "text",
            "code": "text",
            "order": 0
        }
    ]
}
```

### 2 Instruction Document List
```http
/api/student-clubs/instructions/documents/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name_ru": "text",
            "name_en": "text",
            "name_kg": "text",
            "description_ru": "text",
            "description_en": "text",
            "description_kg": "text",
            "category": "text",
            "format": "PDF",
            "size": "2.5 MB",
            "version": "1.0",
            "pages": null,
            "downloads": 0,
            "tags": [
                {
                    "count": 0,
                    "next": null,
                    "previous": null,
                    "results": []
                }
            ],
            "downloadUrl": "/media/instructions/SQL-UPRAVLENIE-DANNYMI-I-STRUKTURAMI_2.pdf",
            "lastUpdated": "Oct 15, 2025"
        }
    ]
}
```
### 3  Important Update List
```http
/api/student-clubs/instructions/updates/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title_ru": "text",
            "title_en": "text",
            "title_kg": "text",
            "description_ru": "text",
            "description_en": "text",
            "description_kg": "text",
            "date": "2025-10-15",
            "order": 0
        }
    ]
}
```

###  e-bilim
### 1 Ebilim System Status List

```http
/api/student-clubs/ebilim/system-status/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "status": "online",
            "status_display": "Online",
            "message": "text",
            "last_update": "2025-10-15T17:33:19.241660Z",
            "support_email": "aktam200e@gmail.com",
            "support_phone": "55555"
        }
    ]
}
```
### 2 Ebilim Stat List
```http
/api/student-clubs/ebilim/stats/
```
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "key": "text",
            "value": "text",
            "label": "text"
        }
    ]
}
```

### 3 Ebilim Quick Link List
```http
/api/student-clubs/ebilim/quick-links/
```
```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "text",
            "url": "http://127.0.0.1:8000/admin/student_clubs/socialnetworkaccount/add/",
            "icon": "📚"
        }
    ]
}
```
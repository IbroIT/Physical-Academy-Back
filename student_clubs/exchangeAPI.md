# Exchange Programs API Documentation

## Overview

This API provides data for exchange programs offered by the university to partner institutions worldwide. It allows students to search, filter, and learn about various exchange opportunities.

## Base URL

All endpoints are relative to: `/api/student-clubs/`

## Authentication

Most endpoints are public and do not require authentication. Admin actions (POST, PUT, DELETE) require authentication.

## Endpoints

### Exchange Page Data

Retrieves all data needed for the exchange programs page in one call.

**URL:** `/exchange-page/`  
**Method:** `GET`  
**Query Parameters:**

- `lang` (optional): Language code (en, ru, kg). Default: en

**Response:**

```json
{
  "title": "International Exchange Programs",
  "subtitle": "Expand your horizons with our partner universities worldwide and gain invaluable international experience",
  "stats": [
    {
      "id": 1,
      "icon": "🌍",
      "value_ru": "25+",
      "value_en": "25+",
      "value_kg": "25+",
      "label_ru": "Стран-партнеров",
      "label_en": "Partner Countries",
      "label_kg": "Өнөктөш өлкөлөр",
      "order": 1
    }
    // More stats...
  ],
  "programs": [
    {
      "id": 1,
      "university_en": "University of California",
      "country_en": "USA",
      "description_en": "Study at one of the world's top universities...",
      "region": 1,
      "region_name": "North America",
      "duration_type": 1,
      "duration_type_name": "Semester",
      "duration_en": "4-6 months",
      "cost": "$5000",
      "language_en": "English",
      "grants_available_en": "Available",
      "deadline": "October 15, 2023",
      "available_spots": 5,
      "icon": "🎓",
      "website": "https://www.university.edu/exchange",
      "difficulty": "medium",
      "difficulty_label_en": "Moderate",
      "is_featured": true,
      "is_active": true,
      "requirements": [
        {
          "id": 1,
          "text_en": "GPA of 3.5 or higher",
          "order": 1
        }
        // More requirements...
      ],
      "benefits": [
        {
          "id": 1,
          "text_en": "Course credit transfer",
          "order": 1
        }
        // More benefits...
      ],
      "available_courses": [
        {
          "id": 1,
          "name_en": "Computer Science"
        }
        // More courses...
      ]
    }
    // More programs...
  ],
  "filters": {
    "regions": [
      {
        "id": 1,
        "name": "North America",
        "code": "north-america"
      }
      // More regions...
    ],
    "durations": [
      {
        "id": 1,
        "name": "Semester",
        "code": "semester"
      }
      // More durations...
    ]
  },
  "deadlines": {
    "title": "Upcoming Deadlines",
    "list": [
      {
        "id": 1,
        "date": "October 15, 2023",
        "program_en": "University of California Exchange",
        "days_left_en": "30 days left",
        "order": 1
      }
      // More deadlines...
    ]
  }
}
```

### Individual Exchange Program Endpoints

#### Exchange Regions

**URL:** `/exchange/regions/`  
**Method:** `GET`  
**Response:** List of available regions for exchange programs.

#### Exchange Duration Types

**URL:** `/exchange/durations/`  
**Method:** `GET`  
**Response:** List of available duration types for exchange programs.

#### Exchange Programs

**URL:** `/exchange/programs/`  
**Method:** `GET`  
**Query Parameters:**

- `lang` (optional): Language code (en, ru, kg). Default: en

**Response:** List of exchange programs with detailed information.

#### Exchange Program Requirements

**URL:** `/exchange/requirements/`  
**Method:** `GET`  
**Query Parameters:**

- `program` (optional): Filter by program ID

**Response:** List of requirements for exchange programs.

#### Exchange Program Benefits

**URL:** `/exchange/benefits/`  
**Method:** `GET`  
**Query Parameters:**

- `program` (optional): Filter by program ID

**Response:** List of benefits for exchange programs.

#### Exchange Program Courses

**URL:** `/exchange/courses/`  
**Method:** `GET`  
**Query Parameters:**

- `program` (optional): Filter by program ID

**Response:** List of available courses in exchange programs.

#### Exchange Page Statistics

**URL:** `/exchange/stats/`  
**Method:** `GET`

**Response:** Statistics displayed on the exchange programs page.

#### Exchange Deadlines

**URL:** `/exchange/deadlines/`  
**Method:** `GET`

**Response:** List of upcoming deadlines for exchange programs.

## Frontend Integration

The frontend component `ExchangePrograms.jsx` expects the following data structure:

1. Page title and subtitle
2. Statistics to display in the top section
3. A list of programs with details like university name, country, duration, requirements, etc.
4. Filter options for regions and duration types
5. Upcoming deadlines

The primary endpoint `/exchange-page/` provides all this data in a single API call, formatted to match the component's expected structure.

# Web of Science API Documentation

## Overview

This document provides comprehensive documentation for the Web of Science API endpoints. The API allows you to retrieve and manage information about Web of Science publications, metrics, categories, and collaborations.

## Base URL

All API endpoints are relative to `/api/science/`.

## Authentication

Authentication is required for write operations (POST, PUT, DELETE). Read operations (GET) may be public depending on configuration.

## Web of Science API Endpoints

### Time Ranges

Time ranges represent different time periods for Web of Science data (e.g., 1 year, 3 years, 5 years, all time).

- **GET** `/wos-time-ranges/` - List all time ranges
- **GET** `/wos-time-ranges/{id}/` - Retrieve a specific time range
- **POST** `/wos-time-ranges/` - Create a new time range
- **PUT** `/wos-time-ranges/{id}/` - Update a time range
- **DELETE** `/wos-time-ranges/{id}/` - Delete a time range

### Metrics

Main metrics for Web of Science (publications, citations, h-index, etc.)

- **GET** `/wos-metrics/` - List all metrics
  - Query params: `?time_range=all` (filter by time range key)
- **GET** `/wos-metrics/{id}/` - Retrieve a specific metric
- **POST** `/wos-metrics/` - Create a new metric
- **PUT** `/wos-metrics/{id}/` - Update a metric
- **DELETE** `/wos-metrics/{id}/` - Delete a metric

### Categories

Publication categories for Web of Science (Physics, Computer Science, Engineering, etc.)

- **GET** `/wos-categories/` - List all categories
  - Query params: `?time_range=all` (filter by time range key)
- **GET** `/wos-categories/{id}/` - Retrieve a specific category
- **POST** `/wos-categories/` - Create a new category
- **PUT** `/wos-categories/{id}/` - Update a category
- **DELETE** `/wos-categories/{id}/` - Delete a category

### Collaborations

International collaborations for Web of Science publications

- **GET** `/wos-collaborations/` - List all collaborations
  - Query params: `?time_range=all` (filter by time range key)
- **GET** `/wos-collaborations/{id}/` - Retrieve a specific collaboration
- **POST** `/wos-collaborations/` - Create a new collaboration
- **PUT** `/wos-collaborations/{id}/` - Update a collaboration
- **DELETE** `/wos-collaborations/{id}/` - Delete a collaboration

### Journal Quartiles

Journal quartiles (Q1, Q2, etc.) for Web of Science publications

- **GET** `/wos-journal-quartiles/` - List all journal quartiles
  - Query params: `?time_range=all` (filter by time range key)
- **GET** `/wos-journal-quartiles/{id}/` - Retrieve a specific journal quartile
- **POST** `/wos-journal-quartiles/` - Create a new journal quartile
- **PUT** `/wos-journal-quartiles/{id}/` - Update a journal quartile
- **DELETE** `/wos-journal-quartiles/{id}/` - Delete a journal quartile

### Additional Metrics

Additional metrics for Web of Science (open access percentage, impact factors, etc.)

- **GET** `/wos-additional-metrics/` - List all additional metrics
  - Query params: `?time_range=all` (filter by time range key)
- **GET** `/wos-additional-metrics/{id}/` - Retrieve a specific additional metric
- **POST** `/wos-additional-metrics/` - Create a new additional metric
- **PUT** `/wos-additional-metrics/{id}/` - Update an additional metric
- **DELETE** `/wos-additional-metrics/{id}/` - Delete an additional metric

### Sections

Text sections for Web of Science page (titles, subtitles, etc.)

- **GET** `/wos-sections/` - List all sections
- **GET** `/wos-sections/{id}/` - Retrieve a specific section
- **POST** `/wos-sections/` - Create a new section
- **PUT** `/wos-sections/{id}/` - Update a section
- **DELETE** `/wos-sections/{id}/` - Delete a section

### Web of Science Page

Complete page data for Web of Science frontend component

- **GET** `/wos-page/` - Get aggregated Web of Science page data
  - Query params:
    - `?time_range=all` (filter by time range key)
    - `?lang=ru` (language for localized content, options: ru, en, kg)

## Response Format

The Web of Science page endpoint returns data in the following format:

```json
{
  "title": "Web of Science Publications",
  "subtitle": "Publications in Web of Science indexed journals",
  "metrics": [
    {
      "id": 1,
      "key": "publications",
      "value": "156",
      "label": "Publications",
      "description": "Total number of publications in Web of Science",
      "icon": "📄",
      "order": 1
    },
    {
      "id": 2,
      "key": "citations",
      "value": "1872",
      "label": "Citations",
      "description": "Total number of citations in Web of Science",
      "icon": "📚",
      "order": 2
    },
    {
      "id": 3,
      "key": "h-index",
      "value": "23",
      "label": "H-index",
      "description": "H-index in Web of Science",
      "icon": "📊",
      "order": 3
    },
    {
      "id": 4,
      "key": "avg-citations",
      "value": "12.5",
      "label": "Average Citations",
      "description": "Average citations per publication",
      "icon": "📈",
      "order": 4
    }
  ],
  "timeRanges": {
    "labels": ["2018", "2019", "2020", "2021", "2022", "2023"],
    "datasets": [
      {
        "label": "Publications",
        "data": [18, 22, 25, 31, 28, 32],
        "borderColor": "rgba(16, 185, 129, 1)",
        "backgroundColor": "rgba(16, 185, 129, 0.2)"
      },
      {
        "label": "Citations",
        "data": [145, 203, 275, 390, 420, 439],
        "borderColor": "rgba(59, 130, 246, 1)",
        "backgroundColor": "rgba(59, 130, 246, 0.2)"
      }
    ]
  },
  "categories": {
    "labels": ["Physics", "Materials Science", "Chemistry", "Engineering", "Computer Science", "Mathematics"],
    "datasets": [
      {
        "data": [42, 38, 32, 25, 12, 7],
        "backgroundColor": [...]
      }
    ]
  },
  "sourceCategories": {
    "labels": ["PHYSICAL REVIEW B", "JOURNAL OF PHYSICS", "APPLIED PHYSICS LETTERS", "SCIENTIFIC REPORTS", "ACS NANO", "OTHERS"],
    "datasets": [
      {
        "data": [28, 23, 19, 15, 12, 59],
        "backgroundColor": [...]
      }
    ]
  },
  "collaborations": [
    {
      "id": 1,
      "country": "USA",
      "flag": "🇺🇸",
      "institutions": 12,
      "publications": 28,
      "order": 1
    },
    {
      "id": 2,
      "country": "Germany",
      "flag": "🇩🇪",
      "institutions": 8,
      "publications": 15,
      "order": 2
    }
  ],
  "topJournals": {
    "labels": ["Q1", "Q2", "Q3", "Q4"],
    "datasets": [
      {
        "data": [68, 45, 32, 11],
        "backgroundColor": [...],
        "borderColor": [...]
      }
    ]
  },
  "additionalMetrics": [
    {
      "id": 1,
      "key": "open-access",
      "value": "42%",
      "title": "Open Access",
      "description": "Percentage of publications available in open access",
      "icon": "🔓",
      "order": 1
    },
    {
      "id": 2,
      "key": "international",
      "value": "65%",
      "title": "International Co-authored",
      "description": "Percentage of publications with international co-authors",
      "icon": "🌎",
      "order": 2
    }
  ],
  "categoriesTitle": "Publications by Category",
  "collaborationsTitle": "International Collaborations",
  "collaborationsInstitutions": "institutions",
  "collaborationsPublications": "publications",
  "topJournalsTitle": "Publications by Journal Quartile",
  "topJournalsPublications": "publications",
  "timelineTitle": "Publications & Citations Over Time"
}
```

## Frontend Integration

To integrate with the frontend, update the following files:

### 1. src/services/api.js

Add the following method to the ApiService class:

```javascript
// Web of Science API methods
async getWebOfSciencePage(language) {
  return this.request(`/science/wos-page/?lang=${this.mapLanguage(language)}`);
}
```

### 2. src/hooks/useApi.js

Add the following method to the useApi hook:

```javascript
// Get Web of Science page data
const getWebOfSciencePage = async () => {
  try {
    return await apiService.getWebOfSciencePage(i18n.language);
  } catch (error) {
    console.error("Error fetching Web of Science data:", error);
    throw error;
  }
};

// And include it in the returned object:
return {
  // ... existing methods
  getWebOfSciencePage,
};
```

### 3. WebOfScience.jsx

Replace the mock data in the useEffect with actual API call:

```javascript
useEffect(() => {
  const fetchData = async () => {
    setLoading(true);
    setError(null);

    try {
      // Replace the mock data with the actual API call
      const response = await apiService.getWebOfSciencePage(i18n.language);
      setData(response);
      setLoading(false);
    } catch (err) {
      console.error("Error fetching Web of Science data:", err);
      setError(err.message || "Failed to load Web of Science data");
      setLoading(false);
    }
  };

  fetchData();
}, [i18n.language]);
```

## Data Management

To manage the Web of Science data:

1. Create time ranges first (e.g., 'all', '5y', '3y', '1y')
2. Add metrics, categories, collaborations, etc. for each time range
3. Add sections for page titles and other text content

This ensures the data is properly organized and can be filtered by time range when displayed on the frontend.

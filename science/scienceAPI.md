# Science API Documentation

## Publications API

### Get Publications Page Data

Retrieves complete data for the publications page including stats, featured publications, and regular publications.

```
GET /api/science/publications-page/
```

Query Parameters:

- `lang` (string): Language code (ru, en, kg). Default: ru
- `search` (string, optional): Search term for filtering publications
- `type` (string, optional): Filter by publication type

Response:

```json
{
  "stats": [
    {
      "id": 1,
      "label": "Total Publications",
      "value": "150+",
      "icon": "📚",
      "order": 1
    }
  ],
  "featured": [
    {
      "id": 1,
      "title": "Featured Publication Title",
      "authors": "Author Names",
      "journal": "Journal Name",
      "year": 2023,
      "citation_count": 10,
      "impact_factor": 2.5,
      "abstract": "Publication abstract...",
      "doi": "10.1000/xyz123",
      "url": "https://...",
      "pdf_url": "https://...",
      "publication_type": "article",
      "is_featured": true,
      "order": 1
    }
  ],
  "publications": [
    {
      "id": 2,
      "title": "Regular Publication Title"
      // ... same fields as featured
    }
  ]
}
```

### Get Publications List

Retrieves a list of publications with optional filtering.

```
GET /api/science/publications/
```

Query Parameters:

- `lang` (string): Language code (ru, en, kg). Default: ru
- `search` (string, optional): Search term
- `type` (string, optional): Publication type
- `year` (number, optional): Filter by year
- `featured` (boolean, optional): Filter featured publications

### Get Publication by ID

Retrieves a single publication by its ID.

```
GET /api/science/publications/{id}/
```

Query Parameters:

- `lang` (string): Language code (ru, en, kg). Default: ru

### Get Publication Statistics

Retrieves publication statistics.

```
GET /api/science/publication-stats/
```

Query Parameters:

- `lang` (string): Language code (ru, en, kg). Default: ru

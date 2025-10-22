# E-learning System API Documentation

## 1. E-learning Stats List

```http
GET /api/student-clubs/ebilim/stats/
```

Returns list of statistics for the e-learning system.

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "key": "active_courses",
      "value": "1000+",
      "label": "Active Courses"
    }
  ]
}
```


## 2. E-learning Quick Links List

```http
GET /api/student-clubs/ebilim/quick-links/
```

Returns list of quick access links for the e-learning platform.

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "My Courses",
      "url": "https://elearning.example.com/courses",
      "icon": "📚"
    }
  ]
}
```

## 3. E-learning System Status

```http
GET /api/student-clubs/ebilim/system-status/
```

Returns current system status and support information.

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "status": "online",
      "status_display": "Online",
      "message": "System is operating normally",
      "last_update": "2025-10-15T12:00:00Z",
      "support_email": "support@example.com",
      "support_phone": "+1234567890"
    }
  ]
}
```

## 4. E-learning Page Data

```http
GET /api/student-clubs/ebilim/
```

Returns combined data for the e-learning page, including stats, quick links, and system status.

```json
{
  "stats": [
    {
      "key": "active_courses",
      "value": "1000+",
      "label": "Active Courses"
    }
  ],
  "quick_links": [
    {
      "name": "My Courses",
      "url": "https://elearning.example.com/courses",
      "icon": "📚"
    }
  ],
  "system_status": {
    "status": "online",
    "status_display": "Online",
    "message": "System is operating normally",
    "last_update": "2025-10-15T12:00:00Z",
    "support_email": "support@example.com",
    "support_phone": "+1234567890"
  }
}
```

# Student Scientific Society API Documentation

## Overview

This documentation describes the API endpoints for the Student Scientific Society section of the application. The API provides access to information about the society, its projects, events, leadership, and more.

## Base URL

All API endpoints are relative to `/api/science/`

## Authentication

No authentication is required for read-only access to these endpoints.

## Available Endpoints

### Complete Page Data

```
GET /student-scientific-society-page/
```

Returns a complete data set for the Student Scientific Society page, including:

- Basic information
- Statistics
- About section features
- Projects with tags
- Events
- Join steps
- Leadership information
- Contacts
- Upcoming events

### Basic Information

```
GET /sss-info/
```

Returns basic information about the Student Scientific Society, including titles and descriptions for different sections of the page.

### Statistics

```
GET /sss-stats/
```

Returns statistics about the Student Scientific Society.

### Features

```
GET /sss-features/
```

Returns features presented in the "About" section.

### Projects

```
GET /sss-projects/
```

Returns projects of the Student Scientific Society.

### Events

```
GET /sss-events/
```

Returns all events related to the Student Scientific Society.

Query Parameters:

- `status`: Filter events by status (values: "upcoming", "completed")

Example:

```
GET /sss-events/?status=upcoming
```

### Join Steps

```
GET /sss-join-steps/
```

Returns steps required to join the Student Scientific Society.

### Leadership

```
GET /sss-leadership/
```

Returns information about leadership members of the Student Scientific Society.

### Contacts

```
GET /sss-contacts/
```

Returns contact information for the Student Scientific Society.

## Data Models

### Info

```json
{
  "id": 1,
  "title": "Student Scientific Society",
  "subtitle": "Fostering scientific innovation and research among students",
  "about_title": "About Us",
  "about_description": "Our society promotes scientific research...",
  "projects_title": "Our Projects",
  "events_title": "Events",
  "join_title": "How to Join",
  "leadership_title": "Our Leadership",
  "contacts_title": "Contact Us",
  "upcoming_events_title": "Upcoming Events"
}
```

### Stat

```json
{
  "id": 1,
  "label": "Members",
  "value": "250+"
}
```

### Feature

```json
{
  "id": 1,
  "title": "Research Opportunities",
  "description": "Access to laboratories and research facilities",
  "icon": "🔬"
}
```

### Project

```json
{
  "id": 1,
  "name": "Bioengineering Innovations",
  "short_description": "Research in bioengineering field",
  "description": "This project explores innovative approaches to bioengineering...",
  "icon": "🧬",
  "tags": [
    { "id": 1, "name": "Bioengineering" },
    { "id": 2, "name": "Innovation" }
  ]
}
```

### Event

```json
{
  "id": 1,
  "name": "Annual Scientific Conference",
  "description": "Annual conference showcasing student research",
  "icon": "🎯",
  "date": "2025-11-15",
  "time": "10:00-16:00",
  "status": "upcoming",
  "status_display": "Upcoming",
  "days_left": 30
}
```

### Join Step

```json
{
  "id": 1,
  "step": 1,
  "title": "Submit Application",
  "description": "Complete and submit the online application form"
}
```

### Leader

```json
{
  "id": 1,
  "name": "John Doe",
  "position": "President",
  "department": "Computer Science Department"
}
```

### Contact

```json
{
  "id": 1,
  "label": "Email",
  "value": "sss@example.com",
  "icon": "✉️"
}
```

## Language Support

The API supports multiple languages (Russian, English, and Kyrgyz). The language is determined by the Accept-Language header in the request. If no language is specified, Russian is used as the default.

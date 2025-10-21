# Instructions API Documentation

## Overview

This API provides access to academic instruction documents, their categories, and important updates. It supports multilingual content (en, ru, kg) and document management.

## Base URL

All endpoints are relative to: `/api/student-clubs/`

## Authentication

Most endpoints are public and do not require authentication. Admin actions (POST, PUT, DELETE) require authentication.

## Endpoints

### Instructions Page Data

Retrieves all data needed for the instructions page in one call.

**URL:** `/instructions-page/`  
**Method:** `GET`  
**Query Parameters:**

- `lang` (optional): Language code (en, ru, kg). Default: en

**Response:**

```json
{
  "title": "Instructions and Documents",
  "subtitle": "Academic documents and instructions for students and staff",
  "categories": {
    "academic": "Academic",
    "admission": "Admission",
    "financial": "Financial",
    "general": "General"
  },
  "documents": [
    {
      "id": 1,
      "name": "Student Handbook 2025",
      "description": "Complete guide for students...",
      "category": "academic",
      "format": "PDF",
      "size": "2.5 MB",
      "version": "1.0",
      "pages": 45,
      "downloads": 123,
      "tags": ["handbook", "guide", "rules"],
      "downloadUrl": "/media/instructions/handbook.pdf",
      "lastUpdated": "Oct 15, 2025"
    }
  ],
  "importantUpdates": [
    {
      "id": 1,
      "title": "New Document Upload System",
      "description": "We have updated our document...",
      "date": "Oct 15, 2025"
    }
  ]
}
```

### Individual Endpoints

#### Instruction Categories

**URL:** `/instructions/categories/`  
**Method:** `GET`  
**Response:** List of available document categories.

#### Instruction Documents

**URL:** `/instructions/documents/`  
**Method:** `GET`  
**Query Parameters:**

- `category` (optional): Filter by category code

**Response:** List of instruction documents.

#### Important Updates

**URL:** `/instructions/updates/`  
**Method:** `GET`

**Response:** List of important updates.

## Document Download Count

The download count for documents is automatically incremented when retrieving a single document via:

```
GET /instructions/documents/{id}/
```

This endpoint returns the full document details and increments the download counter.

## Frontend Integration

The frontend component `Instructions.jsx` expects:

1. Page title and subtitle (localized)
2. Document categories for filtering
3. List of documents with:
   - Basic info (name, description)
   - File details (format, size, version)
   - Download URL
   - Stats (downloads, last updated)
   - Tags
4. Important updates with:
   - Title
   - Description
   - Display date

The primary endpoint `/instructions-page/` provides all this data in a single API call, formatted to match the component's expected structure.

## Media Files

Document files are served from:

```
MEDIA_URL/instructions/
```

Make sure your Django settings include proper media file handling and your web server is configured to serve these files.

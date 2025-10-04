# Academy Management System - Backend

Django REST API backend for the Academy Management System's "About Section".

## Features

- **Leadership Management**: API for academy leadership information
- **Accreditations**: Management of certificates and accreditations
- **Organization Structure**: Hierarchical organization structure
- **Documents**: Downloadable documents management
- **Multilingual Support**: Russian, Kyrgyz, and English
- **REST API**: Full REST API with Django REST Framework
- **Interactive Documentation**: Swagger UI and ReDoc
- **Admin Interface**: Django admin for content management

## Technology Stack

- Django 5.1.2
- Django REST Framework 3.15.2
- PostgreSQL/SQLite
- Python 3.13+

## Quick Start

### 1. Clone and Setup

```bash
cd ac_back
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser  # Optional: for admin access
```

### 4. Run Development Server

```bash
python manage.py runserver
```

### 5. Access the API

- **API Base URL**: http://localhost:8000/api/v1/
- **Admin Interface**: http://localhost:8000/admin/
- **API Documentation**: http://localhost:8000/api/docs/
- **ReDoc Documentation**: http://localhost:8000/api/redoc/

## API Endpoints

### Leadership
- `GET /api/v1/leadership/` - List all leadership members
- `GET /api/v1/leadership/{id}/` - Get specific leadership member
- `GET /api/v1/leadership/directors/` - Get directors only
- `GET /api/v1/leadership/department-heads/` - Get department heads

### Accreditations
- `GET /api/v1/accreditations/` - List all accreditations
- `GET /api/v1/accreditations/{id}/` - Get specific accreditation
- `GET /api/v1/accreditations/active/` - Get valid accreditations only

### Organization Structure
- `GET /api/v1/organization-structure/` - List all departments
- `GET /api/v1/organization-structure/{id}/` - Get specific department
- `GET /api/v1/organization-structure/hierarchy/` - Get hierarchical structure

### Documents
- `GET /api/v1/documents/` - List all downloadable documents
- `GET /api/v1/documents/{id}/` - Get specific document

## Multilingual Support

Add `?lang=en` or `?lang=ky` to any endpoint for localized content:

```bash
curl "http://localhost:8000/api/v1/leadership/?lang=en"
curl "http://localhost:8000/api/v1/leadership/?lang=ky"
```

## Features

### Filtering and Search
```bash
# Filter by leadership type
GET /api/v1/leadership/?leadership_type=director

# Search across multiple fields
GET /api/v1/leadership/?search=John

# Order results
GET /api/v1/leadership/?ordering=name
```

### Pagination
```bash
# Custom page size
GET /api/v1/leadership/?page_size=50

# Navigate pages
GET /api/v1/leadership/?page=2
```

## Admin Interface

Access the admin interface at http://localhost:8000/admin/ to manage:
- Leadership members
- Accreditations
- Organization structure
- Downloadable documents

## File Structure

```
ac_back/
├── ac_back/                 # Main project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── about_section/          # Main app
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URL configuration
│   └── admin.py           # Admin configuration
├── media/                 # Uploaded files
├── static/               # Static files
├── requirements.txt      # Python dependencies
└── manage.py            # Django management script
```

## Development

### Adding New Features

1. Create/modify models in `about_section/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Update serializers in `about_section/serializers.py`
5. Update views in `about_section/views.py`
6. Update URLs in `about_section/urls.py`

### Environment Variables

Create a `.env` file for production settings:

```
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Production Deployment

### Database Configuration

For production, configure PostgreSQL in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'academy_db',
        'USER': 'academy_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files

```bash
python manage.py collectstatic
```

### Security Settings

Update these settings for production:
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use strong `SECRET_KEY`
- Set up HTTPS
- Configure proper database

## Contributing

1. Create a feature branch
2. Make changes
3. Add tests if applicable
4. Update documentation
5. Submit a pull request

## License

[Your License Here]

## Support

For questions or issues, please contact the development team.
# How to Apply the Scholarship and Visa Support Implementation

This guide explains how to apply the changes for the Scholarship and Visa Support features that have been implemented.

## 1. Apply Backend Changes

### Step 1: Apply Database Migrations

Run the following commands to create and apply migrations for the new models:

```bash
python manage.py makemigrations student_clubs
python manage.py migrate
```

### Step 2: Create Initial Data

Access the Django admin interface at `http://localhost:8000/admin/` and:

1. Create scholarship programs:

   - Navigate to "Scholarship programs" section
   - Add at least one program with all required fields
   - Add required documents for each program

2. Create visa support services:
   - Navigate to "Визовая поддержка" section
   - Add multiple services, marking some as "featured" for highlight sections
   - Add contact persons for visa support

## 2. Verify API Endpoints

Test the following API endpoints to ensure they're working correctly:

- `/api/student-clubs/scholarship/page_data/?lang=ru`
- `/api/student-clubs/scholarship/programs/?lang=ru`
- `/api/student-clubs/scholarship/documents/?lang=ru`
- `/api/student-clubs/visa-support/page_data/?lang=ru`
- `/api/student-clubs/visa-support/services/?lang=ru`
- `/api/student-clubs/visa-support/contacts/?lang=ru`

## 3. Frontend Integration Testing

1. Make sure the frontend API service is correctly pointing to your backend server:

   - Check `src/services/api.js` and ensure `this.baseURL` is correct

2. Test the scholarship page:

   - Navigate to `/students/scholarship`
   - Verify data is loading from API
   - Check that error handling works correctly

3. Test the visa support page:

   - Navigate to `/students/visa-support`
   - Verify data is loading from API
   - Check that error handling works correctly

4. Test multilingual support:
   - Change language and verify content changes accordingly
   - Test for Russian (ru), English (en), and Kyrgyz (kg)

## Troubleshooting

### API Connection Issues

- Check that backend server is running
- Verify CORS settings in Django settings.py
- Check network tab in browser developer tools for errors

### Missing Data

- Make sure you've created data in the admin interface
- Check that fields with `is_active=True` are being used
- Verify language parameters are being passed correctly

### Frontend Display Issues

- Check console for JavaScript errors
- Verify component structure matches expected API response format
- Test fallback mechanisms by temporarily disabling API

## Support

If you encounter issues with this implementation, please refer to:

- The API documentation in `student_clubs/scholarshipAPI.md`
- The implementation summary in `SCHOLARSHIP_VISA_IMPLEMENTATION.md`

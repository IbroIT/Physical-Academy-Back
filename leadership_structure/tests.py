from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import (
    BoardOfTrustees, AuditCommission, AcademicCouncil,
    Commission, AdministrativeDepartment, AdministrativeUnit
)


class LeadershipStructureAPITestCase(APITestCase):
    """Test cases for Leadership Structure API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        # Create test Board of Trustees member
        self.trustee = BoardOfTrustees.objects.create(
            name="Test Trustee",
            name_kg="Тест Попечитель",
            name_en="Test Trustee EN",
            position="Chairman",
            position_kg="Председатель",
            position_en="Chairman EN",
            bio="Test bio",
            bio_kg="Тест биография",
            bio_en="Test bio EN",
            email="test@example.com",
            is_active=True,
            order=1
        )
    
    def test_list_board_of_trustees(self):
        """Test listing Board of Trustees members"""
        response = self.client.get('/api/leadership-structure/board-of-trustees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_multilanguage_support(self):
        """Test multilanguage support"""
        # Test Russian (default)
        response = self.client.get('/api/leadership-structure/board-of-trustees/')
        self.assertEqual(response.data[0]['name'], "Test Trustee")
        
        # Test Kyrgyz
        response = self.client.get('/api/leadership-structure/board-of-trustees/?lang=kg')
        self.assertEqual(response.data[0]['name'], "Тест Попечитель")
        
        # Test English
        response = self.client.get('/api/leadership-structure/board-of-trustees/?lang=en')
        self.assertEqual(response.data[0]['name'], "Test Trustee EN")


# Add more tests as needed

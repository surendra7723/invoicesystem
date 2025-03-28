from django.test import TestCase
from .models import Company

class CompanyModelTest(TestCase):
    def setUp(self):
        Company.objects.create(name="Test Company", category="TECH", email="test@example.com")

    def test_company_creation(self):
        company = Company.objects.get(name="Test Company")
        self.assertEqual(company.category, "TECH")
        self.assertEqual(company.email, "test@example.com")

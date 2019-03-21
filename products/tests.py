from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTestCase(TestCase):
    """
        Test suite for the products views and models
    """
    def setUp(self):
        """ Set up the default/sample product"""
        Product.objects.create(name='Kiwi',price=500)
    
    def test_1_product_created(self):
        """ Test that the Product models allows for creation of a product"""
        self.assertEqual(Product.objects.count(), 1)

    def test_2_product_model_str(self):
        """ Test the model string representation method"""
        self.assertEqual(Product.objects.get(name="Kiwi").__str__(),'Kiwi - 500')

    def test_3_product_deleted(self):
        """Test the deletion of a product from the model"""
        Product.objects.get(name='Kiwi').delete()
        self.assertEqual(Product.objects.count(), 0)

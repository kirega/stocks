from django.test import TestCase
from .models import Store

# Create your tests here.
class StoreTestCase(TestCase):
    """
        Test suite for the store views and models
    """
    def setUp(self):
        """ Set up the default/sample store"""
        Store.objects.create(name='Main',location='Nairobi')
    
    def test_1_store_created(self):
        """ Test that the store models allows for creation of a product"""
        self.assertEqual(Store.objects.count(), 1)

    def test_2_store_model_str(self):
        """ Test the model string representation method"""
        self.assertEqual(Store.objects.get(name="Main").str(),'Main - Nairobi')

    def test_3_store_deleted(self):
        """Test the deletion of a store from the model"""
        Store.objects.get(name='Main').delete()
        self.assertEqual(Store.objects.count(), 0)

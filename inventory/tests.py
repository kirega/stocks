from django.test import TestCase
from .models import Inventory
from stores.models import Store
from products.models import Product
# Create your tests here.
class InventoryTestCase(TestCase):
    """
        Test suite for the inventory views and models
    """
    def setUp(self):
        """ Set up the default/sample inventory"""
        self.product = Product.objects.create(name='Kiwi',price=500)
        self.store = Store.objects.create(name='Main',location='Nairobi')
        Inventory.objects.create(store=self.store, product=self.product,quantity=100)
    
    def test_1_inventory_created(self):
        """ Test that the inventory models allows for creation of a product"""
        self.assertEqual(Inventory.objects.count(), 1)

    def test_2_inventory_model_str(self):
        """ Test the model string representation method"""
        self.assertEqual(Inventory.objects.get(store=self.store,product=self.product).__str__(),'Main-Kiwi-100')

    def test_3_inventory_deleted(self):
        """Test the deletion of a store from the model"""
        Inventory.objects.get(store=self.store,product=self.product).delete()
        self.assertEqual(Inventory.objects.count(), 0)

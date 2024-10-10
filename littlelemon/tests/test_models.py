from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create( title='IceCream', price = 80, inventory=100 )
        
    def test_str_item(self):
        self.assertEqual(str(self.item),"IceCream : 80")

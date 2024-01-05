from django.test import TestCase
from LittleLemonAPI.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=4)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
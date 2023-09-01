from django.test import TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Momo', price = 10, inventory =100)
        Menu.objects.create(title='Choemwin', price = 8, inventory =100)
        Menu.objects.create(title='Jhol Momo', price = 12, inventory =100)

    def test_getall(self):
        menuItem = Menu.objects.get(title='Momo')
        serialized_item = MenuSerializer(menuItem)
        self.assertEqual(serialized_item.data['title'], menuItem.title)
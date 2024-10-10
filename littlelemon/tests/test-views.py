from rest_framework.test import APITestCase
from restaurant.views import MenuItemView , Menu, MenuSerializer
from django.urls import reverse
from rest_framework import status
class MenuItemTest(APITestCase):
    def setUp(self) -> None:
        self.menu1 = Menu.objects.create( title='IceCream', price = 80, inventory=100 )
        self.menu2 = Menu.objects.create( title='burger', price = 60, inventory=50 )
        self.list_url = reverse('menu_list')
    def test_getall(self):
        response = self.client.get(self.list_url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many = True)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)
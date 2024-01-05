# Inside test_views.py
from django.test import TestCase
from django.urls import reverse
from LittleLemonAPI.models import Menu  # Import your Menu model

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu for the view tests
        Menu.objects.create(title="Dish1", price=20, inventory=50)
        Menu.objects.create(title="Dish2", price=30, inventory=70)

    def test_getall(self):
        # URL for the Menu endpoint, adjust this based on your project's URL structure
        url = reverse('restaurant:menu')  # Assuming 'menu-list' is the name of the URL pattern for listing Menu items

        # Make a GET request to the Menu endpoint
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Retrieve the serialized data from the response
        data = response.json()

        # Check if the length of the data matches the number of Menu items created in setUp
        self.assertEqual(len(data), 2)

        # You can add more specific assertions based on your application logic
        # For example, check if certain fields are present in the serialized data

        # Example: Check if the first item has the expected title
        self.assertEqual(data[0]['title'], "Dish1")

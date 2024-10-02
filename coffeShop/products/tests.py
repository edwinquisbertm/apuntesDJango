from django.urls import reverse
from django.test import TestCase

from products.models import Product


# Create your tests here.
class ProductListViewTest(TestCase):
    def test_shoult_return_200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        # breakpoint() esta es una forma de hacer un debug en python y django nos permite hacerlo en cualquier parte del codigo para ver que esta pasando en ese punto del codigo
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 0)

    def test_shoult_return_200_whit_products(self):
        url = reverse("list_product")
        Product.objects.create(
            name="Coca Cola",
            description="Refresco de cola",
            price="1.50",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)

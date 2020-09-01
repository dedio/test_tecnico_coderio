from django.test import TestCase
from swapi.models import Swapi

class SwapiModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Swapi.objects.create(rating = 5, idcharacter = 1)

    def test_rating_label(self):
        swapi = Swapi.objects.get(id=1)
        field_label = swapi._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_idcharacter_label(self):
        swapi = Swapi.objects.get(id=1)
        field_label = swapi._meta.get_field('idcharacter').verbose_name
        self.assertEquals(field_label, 'idcharacter')

from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class SwapiViewTest(APITestCase):
    client = APIClient()

    @classmethod
    def test_view_url_get(self):
        for idcharacter in ['1', 'v', '7667757767']:
            self.client.get('/character/', {'idcharacter': idcharacter}, format ='json')

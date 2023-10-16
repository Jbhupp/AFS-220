from django.test import TestCase

# Create your tests here.
from django.test import Client


class PageViewTests(TestCase):

    c = Client()

    def test_page_status_code(self):
        response = self.c.get('/about', follow= True)
        self.assertEquals(response.status_code, 200)
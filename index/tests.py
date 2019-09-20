from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate

class MainPageTest(TestCase):
    def test_uses_index_template(self):
        activate('en')
        response = self.client.get(reverse("main_page"))
        self.assertTemplateUsed(response, "index.html")
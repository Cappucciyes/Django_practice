from django.test import SimpleTestCase # was told that SimpleTestCase is more appropriate when testing for pages with no models
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_used_hompage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(
        view.func.__name__,
        HomePageView.as_view().__name__
        )

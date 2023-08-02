from django.test import TestCase
from django.urls import reverse, resolve
from .models import Schedule
from .forms import ScheduleForm
from django.contrib.auth import get_user_model
from datetime import datetime
from .views import CreateSchedule


# test for Schedule models and its webpage
class ScheduleTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.testUser = User.objects.create_user(
            username='test',
            email='test@email.com',
            password='testpass123',
        )

        self.testSchedule = Schedule.objects.create(
             title='test title',
             owner=self.testUser,
             what='test what',
             when=datetime(2001,2,3),
        )

        self.response = self.client.get(self.testSchedule.get_absolute_url())

    # checks if schedule can be created with no error
    def test_create_schedule(self):
        self.assertEqual(self.testSchedule.title, 'test title')
        self.assertEqual(self.testSchedule.owner, self.testUser)
        self.assertEqual(self.testSchedule.what, 'test what')
        self.assertEqual(self.testSchedule.when, datetime(2001,2,3))
    
    # checks if correct template is rendered and correct schedule will be loaded
    def test_schedule_detail(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "schedules/schedule_detail.html")
        self.assertContains(self.response, "Schedule Details")
        self.assertNotContains(self.response, "Make New Schedule")

# test for Schedule forms and its webpage
class ScheduleFormTests(TestCase):
    def setUp(self):
            create_url = reverse('schedule_create')
            self.create_response = self.client.get(create_url)

            User = get_user_model()
            self.testUser = User.objects.create_user(
                username='test',
                email='test@email.com',
                password='testpass123',
            )

            # log in
            self.client.login(username='test',password='testpass123')

    def test_create_template(self):
        # checks if correct template is rendered
        self.assertEqual(self.create_response.status_code, 200)
        self.assertTemplateUsed(self.create_response, "schedules/schedule_create.html")
        self.assertContains(self.create_response, "Make New Schedule")
        self.assertNotContains(self.create_response, "Schedule Details")

    def test_create_form(self):

        # checks if correct form is rendered and if rendered html has csrf token
        form = self.create_response.context.get('form')
        self.assertIsInstance(form, ScheduleForm)
        self.assertContains(self.create_response, 'csrfmiddlewaretoken')

        # checks if schedule creation with this form works(user submits form, the view will automatically add user as owner, view returns urls to created schedule)
        create_responce = self.client.post(
            reverse('schedule_create'), 
            data = {
                "title" : "create test title",
                "what" : "create test what",
                "when" : datetime(2001,2,3),
            }
        )
        instance = Schedule.objects.get(title='create test title')
        self.assertEqual(instance.owner, self.testUser)


    def test_create_view(self):
        view = resolve('/schedule/create/')
        self.assertEqual(
            view.func.__name__,
            CreateSchedule.as_view().__name__,
        )
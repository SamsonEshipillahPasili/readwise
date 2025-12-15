from django.test import TestCase
from . import models
from faker import Faker

class CreateAccountRequestManagerTest(TestCase):

    def setUp(self) -> None:
        self.fake = Faker()
    
    def test_create_account(self) -> None:
        request = models.CreateAccountRequest.objects.create_request(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            username=self.fake.user_name(),
            email=self.fake.email(),
            password=self.fake.password(10)
        )

        saved_request = models.CreateAccountRequest.objects.get(pk=request.id)
        self.assertEqual(request.first_name, saved_request.first_name)
        self.assertEqual(request.last_name, saved_request.last_name)
        self.assertEqual(request.username, saved_request.username)
        self.assertEqual(request.email, saved_request.email)
        self.assertEqual(request.password, saved_request.password)

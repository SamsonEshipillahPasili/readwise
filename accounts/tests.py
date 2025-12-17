import datetime as dt

from django.test import TestCase
from django.utils import timezone

from . import models
from .forms import CreateAccountRequestForm
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


class CreateAccountRequestTest(TestCase):

    def setUp(self) -> None:
        self.fake = Faker()

        # create a request to be used for testing.
        self.request = models.CreateAccountRequest.objects.create_request(
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            username=self.fake.user_name(),
            email=self.fake.email(),
            password=self.fake.password(10)
        )

    def test_default_validity(self) -> None:
        # the default factory produces a valid request.
        self.assertTrue(self.request.is_valid())
    
    def test_mark_used(self) -> None:
        # mark the request as used.
        self.request.mark_used()

        # ensure the model is synced with db
        self.request.refresh_from_db()

        # check that the request is invalid.
        self.assertFalse(self.request.is_valid())
    
    def test_expiration(self) -> None:
        # set the created_at to 3 days in the past.
        self.request.created_at = timezone.now() - dt.timedelta(days=3) 
        self.request.save(update_fields=['created_at'])

        # the request should be invalid.
        self.assertFalse(self.request.is_valid())


class CreateAccountRequestFormTest(TestCase):

    def setUp(self) -> None:
        self.fake = Faker()

        self.valid_data = {
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": "strongpass123",
            "confirm_password": "strongpass123",
        }

    def test_form_valid(self):
        form = CreateAccountRequestForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_password_too_short(self):
        data = self.valid_data.copy()
        data["password"] = "short"
        data["confirm_password"] = "short"

        form = CreateAccountRequestForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)
        self.assertEqual(
            form.errors["password"][0],
            "Password should have a minimum of 8 characters."
        )

    def test_passwords_do_not_match(self):
        data = self.valid_data.copy()
        data["confirm_password"] = "differentpass123"

        form = CreateAccountRequestForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn("confirm_password", form.errors)
        self.assertEqual(
            form.errors["confirm_password"][0],
            "The passwords do not match."
        )

    def test_duplicate_email(self):
        models.ReadWiseUser.objects.create(
            username="existing_user",
            email=self.valid_data["email"]
        )

        form = CreateAccountRequestForm(data=self.valid_data)

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
        self.assertEqual(
            form.errors["email"][0],
            "This email is taken."
        )

    def test_duplicate_username(self):
        models.ReadWiseUser.objects.create(
            username=self.valid_data["username"],
            email="other@email.com"
        )

        form = CreateAccountRequestForm(data=self.valid_data)

        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertEqual(
            form.errors["username"][0],
            "Username is taken."
        )


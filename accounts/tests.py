from django.test import TestCase
from . import models

class CreateAccountRequestTest(TestCase):

    def test_is_valid(self) -> None:
        req1 = models.CreateAccountRequest.objects.create()


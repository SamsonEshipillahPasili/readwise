from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from readwise.models import TimestampedModel

class ReadWiseUser(AbstractUser):
    """
    This is the custom user model for all ReadWise users.
    """
    ...

class CreateAccountRequest(TimestampedModel):
    """
    Represents the information the user sends when they 
    create an account before email verification.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid4)
    is_token_used = models.BooleanField(default=False)

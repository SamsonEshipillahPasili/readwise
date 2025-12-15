from uuid import uuid4
import datetime as dt

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

from readwise.models import TimestampedModel

from .managers import CreateAccountRequestManager

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

    objects = CreateAccountRequestManager()

    def is_valid(self) -> bool:
        """
        Checks whether the request is valid. A valid request satisfies the following:-
        - The token hasn't been used before.
        - The token hasn't expired.
        """

        # Token has been used - invalid.
        if self.is_token_used:
            return False

        # Token has expired
        exp_duration_secs = settings.SIGN_UP_TOKEN_EXPIRATION_DURATION_SECS
        expiration_date = self.created_at + dt.timedelta(seconds=exp_duration_secs)
        if timezone.now() > expiration_date:
            return False
        
        return True


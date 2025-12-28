from uuid import uuid4
import datetime as dt

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

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

    def create_account(self) -> ReadWiseUser:
        """
        Creates a ``ReadWise`` account from the registration request.
        Throws a `ValueError` if the request is invalid or another user
        has been saved with the email/username.
        """

        # assert request validity.
        if not self.is_valid():
            raise ValueError('The request has expired or is invalid')

        # assert the username uniqueness
        if ReadWiseUser.objects.filter(username=self.username).exists():
            raise ValueError(f'The username: {self.username} is taken.')
        
        # assert email uniqueness
        if ReadWiseUser.objects.filter(email=self.email).exists():
            raise ValueError(f'The email: {self.email} is taken.')
        
        # mark the as used.
        self.mark_used()
        
        # create the readwise user
        return ReadWiseUser.objects.create(
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username
        )


    def is_valid(self) -> bool:
        """
        Checks whether the request is valid. A valid request satisfies the following:-
        - The token hasn't been used before.
        - The token hasn't expired.

        :return: Whether the current request is valid.
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
    
    def mark_used(self) -> None:
        """
        Mark this request as used.
        """

       # token is marked as used already.
        if self.is_token_used:
            return

        # mark the token as used.
        self.is_token_used = True
        self.save(update_fields=['is_token_used'])
    
    def send_registration_email(self) -> None:
        """
        Send registration email.
        """
        base_url = settings.BASE_URL
        signup_url = f"{base_url}/accounts/complete-signup/{self.token}"

        message = (
            "Welcome to ReadWise!\n\n"
            "Thanks for signing up. To complete your registration, please click "
            "the link below:\n\n"
            f"{signup_url}\n\n"
            "If you did not request this account, you can safely ignore this email.\n\n"
            "— The ReadWise Team"
        )

        send_mail(
            subject='ReadWise Sign Up',
            from_email='admin@readwise.com',
            message=message,
            recipient_list=[self.email]
        )

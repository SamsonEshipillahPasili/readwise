from typing import TYPE_CHECKING

from django.db import models
from django.contrib.auth.hashers import make_password

if TYPE_CHECKING:
    from .models import CreateAccountRequest

class CreateAccountRequestManager(models.Manager):
    """
    Custom manager to handle table-level logic for CreateAccountRequest
    """
    
    def create_request(
        self,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str
    ) -> 'CreateAccountRequest':
        """
        Factory function to generate CreateAccountRequest instances.
        At the moment, the main reason for existence is to hash the supplied password.
        The caller does not need to bother with this detail.

        :param first_name: The user's first name.
        :param last_name: The user's last name.
        :param username: The user's username.
        :param email: The user's email.

        :return: An instance of CreateAccountRequest
        """

        # secure the password
        password = make_password(password)

        # instantiate & save the model
        instance = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        instance.save()

        return instance

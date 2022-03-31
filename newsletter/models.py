from django.db import models


class SigneUp(models.Model):
    """
    Collect user email to receive newsletter
    """
    email = models.EmailField(
        max_length=254,
        unique=True,
        null=False,
        blank=False
    )

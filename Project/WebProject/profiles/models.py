from django.db import models

from django.core.validators import MinLengthValidator
from WebProject.utils.validators import validate_name_starts_with_capital


class Profile(models.Model):
    MAX_LENGTH_NICK = 20
    MIN_LENGTH_NICK = 2
    MIN_LENGTH_NICK_MSG = "Nickname must be at least 2 chars long!"

    MAX_LENGTH_FLNames = 30

    nickname = models.CharField(
        max_length=MAX_LENGTH_NICK,
        unique=True,
        validators=[MinLengthValidator(MIN_LENGTH_NICK, message=MIN_LENGTH_NICK_MSG)]
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_FLNames,
        validators=[validate_name_starts_with_capital],
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_FLNames,
        validators=[validate_name_starts_with_capital],
        verbose_name="Last Name"

    )
    chef = models.BooleanField(
        default=False,
    )
    bio = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nickname
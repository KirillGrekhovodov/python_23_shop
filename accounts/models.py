from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "users"

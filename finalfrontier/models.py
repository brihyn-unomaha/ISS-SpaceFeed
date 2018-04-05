from django.db import models
from django.utils import timezone


class Space(models.Model):
    def __str__(self):
        return self
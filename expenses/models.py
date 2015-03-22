from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    user = models.ForeignKey(User, null=True)

from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    user = models.ForeignKey(User, null=True)
    category = models.ForeignKey(ExpenseCategory, null=True)

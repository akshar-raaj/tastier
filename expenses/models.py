from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

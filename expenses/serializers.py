# This file deals with drf

from .models import Expense
from rest_framework.serializers import ModelSerializer

class ExpenseSerializer(ModelSerializer):
    """
    A Serializer behaves very much like a Form
    A ModelSerializer behaves very much like a ModelForm
    """

    class Meta:
        model = Expense
        fields = ('description', 'amount')

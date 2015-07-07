# This file deals with drf

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseView(APIView):

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

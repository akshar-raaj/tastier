# This file deals with drf

import django_filters

from rest_framework import filters
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(name="amount", lookup_type='gt')
    max_amount = django_filters.NumberFilter(name="amount", lookup_type='lt')

    class Meta:
        model = Expense
        fields = ['min_amount', 'max_amount']

class ExpenseView(generics.ListCreateAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ExpenseFilter
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = super(ExpenseDetailView, self).get_object()
        if not obj.user == self.request.user:
            raise PermissionDenied()
        return obj

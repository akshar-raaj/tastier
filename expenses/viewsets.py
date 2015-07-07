from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from .serializers import ExpenseSerializer
from .models import Expense
from .views import ExpenseFilter


class ExpenseViewSet(ModelViewSet):

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

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

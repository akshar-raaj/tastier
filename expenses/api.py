from tastypie.resources import ModelResource

from .models import Expense

class ExpenseResource(ModelResource):

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        fields = ['description', 'amount']

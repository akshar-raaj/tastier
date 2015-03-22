from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from .models import Expense

class ExpenseResource(ModelResource):

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        fields = ['description', 'amount']
        filtering = {
            'amount': ['gt'],
            'description': ['icontains']
        }
        authorization = Authorization()

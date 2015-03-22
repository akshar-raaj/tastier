from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from .models import Expense

class ExpenseAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

class ExpenseResource(ModelResource):

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        fields = ['description', 'amount']
        filtering = {
            'amount': ['gt'],
            'description': ['icontains']
        }
        authorization = ExpenseAuthorization()
        authentication = ApiKeyAuthentication()

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

from .models import Expense


class ExpenseAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        obj = object_list[0]
        return obj.user == bundle.request.user


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

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields

from .models import Expense, ExpenseCategory


class ExpenseAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        obj = object_list[0]
        return obj.user == bundle.request.user

    def create_detail(self, object_list, bundle):
        user = bundle.request.user
        # Return True if current user is Sheryl else return False
        return user.username == "sheryl"


class ExpenseCategoryResource(ModelResource):
    description = fields.CharField(attribute='description', use_in='detail')

    class Meta:
        queryset = ExpenseCategory.objects.all()
        resource_name = 'expensecategory'
        authorization = Authorization()

class ExpenseResource(ModelResource):
    category = fields.ForeignKey(ExpenseCategoryResource, attribute='category', null=True, full=True)
    description = fields.CharField(attribute='description', use_in='detail')

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        fields = ['description', 'amount', 'category']
        filtering = {
            'amount': ['gt'],
            'description': ['icontains']
        }
        authorization = ExpenseAuthorization()
        authentication = ApiKeyAuthentication()

    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle

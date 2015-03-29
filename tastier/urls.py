from django.conf.urls import patterns, include, url
from django.contrib import admin

from expenses.api import ExpenseResource, ExpenseCategoryResource

expense_resource = ExpenseResource()
expense_category_resource = ExpenseCategoryResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(expense_resource.urls)),
    url(r'^api/', include(expense_category_resource.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

from expenses.api import ExpenseResource

expense_resource = ExpenseResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(expense_resource.urls)),
)

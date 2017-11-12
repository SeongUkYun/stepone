# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^banks/$', views.BankListView.as_view(), name='bank_list'),
    url(r'^bank/create/$', views.BankCreateView.as_view(), name='bank_create'),
    url(r'^bank/(?P<pk>[\d]+)/$', views.BankUpdateView.as_view(), name='bank_update'),
]

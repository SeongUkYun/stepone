# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic

from . import models


class BankListView(generic.ListView):
    model = models.Bank
    template = 'member/bank_list.html'


class BankCreateView(generic.CreateView):
    model = models.Bank
    template = 'member/bank_form.html'
    fields = ['code', 'name']
    success_url = reverse_lazy('staff:member:bank_list')


class BankUpdateView(generic.UpdateView):
    models = models.Bank
    template = 'member/bank.html'

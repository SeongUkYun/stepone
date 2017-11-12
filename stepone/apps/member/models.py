from django.db import models


class Bank(models.Model):
    code = models.CharField('은행코드', max_length=5, unique=True, null=False, blank=False)
    name = models.CharField('은행이름', max_length=10, unique=True, null=False, blank=False)


ACCOUNT_TYPES = (
    ('N', '보통'),
    ('C', '당좌'))


class Account(models.Model):
    bank = models.ForeignKey('Bank', null=False, blank=False)
    type = models.CharField('종류', choices=ACCOUNT_TYPES, max_length=1, null=False, blank=False)
    number = models.CharField('구좌번호', max_length=10, null=False, blank=False)


class Member(models.Model):
    auth = models.OneToOneField('auth.User', related_name='member')
    account = models.OneToOneField('Account')

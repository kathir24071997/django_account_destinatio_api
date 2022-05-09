from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account_Module(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100, null=False, blank=False, verbose_name='Account_ID')
    account_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Account_Name')
    token = models.CharField(max_length=500, blank=False, null=False, verbose_name='Secret_Token')
    website = models.URLField(default='', blank=True, null=True, verbose_name='Account_Website')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date_of_Register')

    class Meta:
        db_table = 'account_module'

    def __str__(self):
        return self.account_name


class Destination_Module(models.Model):
    account = models.ForeignKey(Account_Module, verbose_name='account', on_delete=models.CASCADE)
    app_id = models.CharField(max_length=100, blank=False, null=False, verbose_name='app_id')
    app_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='app_name')
    app_secret = models.CharField(max_length=400, blank=False, null=False, verbose_name='app_secret')
    app_software = models.CharField(max_length=100, blank=True, null=True, verbose_name='app_software')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'destination_module'

    def __str__(self):
        return self.app_id

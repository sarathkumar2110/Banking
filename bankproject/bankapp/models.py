from django.db import models
from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Name must contain only alphabetic characters.')


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    ACCOUNT_CHOICES = (
        ('Savings', 'Savings'),
        ('current', 'Current'),
        ('Fixed', 'Fixed'),
    )

    account = models.CharField(max_length=10, choices=ACCOUNT_CHOICES, default='other')

    def __str__(self):
        return self.account

class BankForm(models.Model):
    name = models.CharField(max_length=100,blank=False, null=False,validators=[validate_name])
    age = models.IntegerField(blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')

    phonenumber = models.CharField(max_length=10,blank=False,null=False)
    mail = models.EmailField(max_length=50,blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    accounttype = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    MATERIAL_CHOICES = (
        ('credit', 'CreditCard'),
        ('debit', 'DebitCard'),
        ('cheque', 'ChequeBook'),
    )

    material = models.CharField(max_length=15, choices=MATERIAL_CHOICES,default='credit')

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




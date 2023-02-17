from celery import shared_task
from datetime import datetime, date
from .models import Account

@shared_task
def check_birthday_discount():
    today = date.today()
    accounts = Account.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)
    for account in accounts:
        account.discount = 50.00
        account.save()

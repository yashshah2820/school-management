# Generated by Django 3.0.5 on 2020-06-25 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='dateofpayment',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='fees',
            name='paymentreceipt',
            field=models.URLField(blank=True),
        ),
    ]

# Generated by Django 3.2 on 2021-05-20 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210520_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 0, 11, 8, 964519)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_launch_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 0, 11, 8, 963510)),
        ),
    ]

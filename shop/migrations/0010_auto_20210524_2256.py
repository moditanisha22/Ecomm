# Generated by Django 3.2 on 2021-05-24 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210524_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 22, 56, 50, 987346)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_launch_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 22, 56, 50, 986343)),
        ),
    ]

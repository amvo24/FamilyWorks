# Generated by Django 3.2.4 on 2024-06-28 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0004_auto_20240628_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 5, 20, 59, 38, 597529, tzinfo=utc)),
        ),
    ]

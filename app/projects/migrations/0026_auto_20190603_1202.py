# Generated by Django 2.2.1 on 2019-06-03 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20190603_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='funding_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 18, 12, 2, 11, 47966)),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

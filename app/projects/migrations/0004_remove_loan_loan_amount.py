# Generated by Django 2.2.1 on 2019-05-03 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_loan_loan_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_amount',
        ),
    ]

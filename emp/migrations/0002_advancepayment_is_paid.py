# Generated by Django 5.0.6 on 2025-01-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancepayment',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]

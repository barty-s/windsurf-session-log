# Generated by Django 5.0.1 on 2024-01-31 08:10

import session_log.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_log', '0019_alter_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(validators=[session_log.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=100, unique_for_date='date'),
        ),
    ]
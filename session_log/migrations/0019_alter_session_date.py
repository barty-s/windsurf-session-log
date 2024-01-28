# Generated by Django 5.0.1 on 2024-01-26 10:52

import session_log.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_log', '0018_alter_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(unique=True, validators=[session_log.models.validate_date]),
        ),
    ]
# Generated by Django 3.2.23 on 2024-01-18 18:25

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_log', '0014_alter_session_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='date'),
        ),
    ]

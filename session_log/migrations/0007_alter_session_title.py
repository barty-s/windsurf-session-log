# Generated by Django 3.2.23 on 2024-01-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_log', '0006_alter_session_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

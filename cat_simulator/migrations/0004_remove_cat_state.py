# Generated by Django 5.0.4 on 2024-04-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_simulator', '0003_cat_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='state',
        ),
    ]
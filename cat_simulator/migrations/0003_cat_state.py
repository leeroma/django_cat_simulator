# Generated by Django 5.0.4 on 2024-04-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_simulator', '0002_alter_cat_fullness_alter_cat_happiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='state',
            field=models.TextField(default='normal'),
        ),
    ]

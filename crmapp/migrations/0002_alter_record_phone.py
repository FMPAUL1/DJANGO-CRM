# Generated by Django 4.2.1 on 2023-06-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railroute', '0003_alter_route_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
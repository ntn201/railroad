# Generated by Django 3.2.2 on 2021-05-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20210519_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20210515_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
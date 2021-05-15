# Generated by Django 3.2.3 on 2021-05-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20210515_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.CharField(default='Customer email', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(default='Customer phone number', max_length=200),
        ),
    ]
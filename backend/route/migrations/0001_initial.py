# Generated by Django 3.2.2 on 2021-05-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('route_name', models.CharField(default='forgoten route', max_length=60)),
            ],
        ),
    ]

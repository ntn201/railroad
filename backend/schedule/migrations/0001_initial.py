# Generated by Django 3.2.2 on 2021-05-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0002_auto_20210516_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrive_order', models.IntegerField(default=1)),
                ('travel_time', models.IntegerField(default=0)),
                ('route_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='route.route')),
            ],
        ),
    ]

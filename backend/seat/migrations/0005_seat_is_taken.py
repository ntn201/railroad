# Generated by Django 3.2.2 on 2021-05-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0004_remove_seat_car_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
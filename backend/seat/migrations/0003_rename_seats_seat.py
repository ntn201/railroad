# Generated by Django 3.2.2 on 2021-05-16 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
        ('seat', '0002_seats_train_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seats',
            new_name='Seat',
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-19 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0006_alter_station_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='station',
            options={'ordering': ['id']},
        ),
    ]
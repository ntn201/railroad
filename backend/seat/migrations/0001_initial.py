# Generated by Django 3.2.2 on 2021-05-20 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField()),
                ('is_taken', models.BooleanField(default=False)),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.train')),
            ],
        ),
    ]

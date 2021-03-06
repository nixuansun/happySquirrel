# Generated by Django 3.0.7 on 2021-04-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='happySquirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=20)),
                ('longitude', models.FloatField(max_length=20)),
                ('unique_squirrel_id', models.CharField(max_length=20)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                ('date', models.CharField(help_text='Date Format: MMDDYYYY', max_length=8)),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=20)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('White', 'White')], max_length=20)),
                ('location', models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], max_length=20)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]

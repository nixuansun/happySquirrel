# Generated by Django 3.0.7 on 2021-04-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='happysquirrel',
            name='color_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='happysquirrel',
            name='other_activities',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='happysquirrel',
            name='other_interactions',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='happysquirrel',
            name='specific_location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='happysquirrel',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=20),
        ),
        migrations.AlterField(
            model_name='happysquirrel',
            name='date',
            field=models.CharField(help_text='Format: YYYY-MM-DD', max_length=8),
        ),
        migrations.AlterField(
            model_name='happysquirrel',
            name='location',
            field=models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], max_length=20),
        ),
        migrations.AlterField(
            model_name='happysquirrel',
            name='primary_fur_color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('White', 'White')], max_length=20),
        ),
    ]

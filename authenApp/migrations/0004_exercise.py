# Generated by Django 4.1.3 on 2023-01-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenApp', '0003_auto_20221230_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseName', models.CharField(max_length=100)),
                ('exerciseType', models.CharField(max_length=100)),
                ('exerciseDecription', models.CharField(max_length=100)),
                ('exerciseRecomendedSets', models.CharField(max_length=10)),
                ('exerciseRecomendedReps', models.CharField(max_length=10)),
            ],
        ),
    ]
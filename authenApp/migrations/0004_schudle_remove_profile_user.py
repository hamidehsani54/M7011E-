# Generated by Django 4.1.4 on 2022-12-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenApp', '0003_alter_trainingprograms_programdifficulty_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='schudle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday', models.CharField(max_length=100)),
                ('Tuesday', models.CharField(max_length=100)),
                ('Wednesday', models.CharField(max_length=100)),
                ('Thursday', models.CharField(max_length=100)),
                ('Friday', models.CharField(max_length=100)),
                ('Saturday', models.CharField(max_length=100)),
                ('Sunday', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]

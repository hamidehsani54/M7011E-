# Generated by Django 4.1.3 on 2022-12-22 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprograms',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenApp.schedule'),
        ),
    ]

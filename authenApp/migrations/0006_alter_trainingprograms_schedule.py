# Generated by Django 4.1.3 on 2023-01-04 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenApp', '0005_alter_exercise_exercisedecription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprograms',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='authenApp.schedule'),
        ),
    ]
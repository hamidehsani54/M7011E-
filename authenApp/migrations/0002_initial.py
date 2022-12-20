from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authenApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programName', models.CharField(max_length=100)),
                ('programDifficulty', models.IntegerField()),
                ('programTrainer', models.CharField(max_length=100)),
                ('programType', models.CharField(max_length=100)),
                ('programDescription', models.CharField(max_length=100)),
            ],
        ),
    ]

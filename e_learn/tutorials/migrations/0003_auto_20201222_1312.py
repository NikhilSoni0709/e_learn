# Generated by Django 3.1.1 on 2020-12-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20201222_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bPriority',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='1', max_length=20),
        ),
    ]

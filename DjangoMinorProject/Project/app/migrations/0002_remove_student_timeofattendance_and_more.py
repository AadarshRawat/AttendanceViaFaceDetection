# Generated by Django 4.0.3 on 2022-04-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='timeofattendance',
        ),
        migrations.AddField(
            model_name='student',
            name='time_of_attendance',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='todays_attendance',
            field=models.CharField(default='A', max_length=100),
        ),
    ]

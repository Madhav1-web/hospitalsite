# Generated by Django 3.1.4 on 2021-02-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210207_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='time',
            field=models.TimeField(max_length=80),
        ),
    ]
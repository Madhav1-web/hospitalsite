# Generated by Django 3.1.4 on 2021-02-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]

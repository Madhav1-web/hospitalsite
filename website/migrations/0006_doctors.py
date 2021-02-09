# Generated by Django 3.1.4 on 2021-02-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_delete_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=80)),
                ('ddept', models.CharField(max_length=80)),
                ('dphone', models.CharField(max_length=80)),
                ('demail', models.CharField(max_length=80)),
                ('dimage', models.ImageField(upload_to='portfolio/images')),
            ],
        ),
    ]

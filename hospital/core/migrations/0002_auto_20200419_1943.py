# Generated by Django 3.0.5 on 2020-04-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]

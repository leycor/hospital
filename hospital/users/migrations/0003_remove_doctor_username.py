# Generated by Django 3.0.5 on 2020-04-14 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
    ]
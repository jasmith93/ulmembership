# Generated by Django 3.2.12 on 2022-11-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]

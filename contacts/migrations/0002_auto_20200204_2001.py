# Generated by Django 2.2.10 on 2020-02-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]

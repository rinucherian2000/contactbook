# Generated by Django 3.2.11 on 2022-06-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
# Generated by Django 3.0.4 on 2021-02-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0011_auto_20210114_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='datefrom',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.0.4 on 2021-01-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20210102_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activated',
            field=models.BooleanField(default=False, verbose_name='Activated'),
        ),
    ]